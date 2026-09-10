#!/bin/bash
set -x

usage() {
    cat <<EOF
Usage: ./create_release.sh [--test] <branch> <release_name>

Tags the given branch and creates (or updates) a GitHub release for it via
the gh CLI. Publishing the release triggers .github/workflows/release.yaml
(on: release: published), which builds the collection from galaxy.yml and
publishes it to Ansible Galaxy.

Arguments:
  --test         Test mode: creates the release as a draft (--draft), which
                 does NOT trigger release.yaml (that only fires on
                 "published"), and skips waiting for/watching the run. Use
                 this for local testing of the tag + release creation flow.
  --previous-tag <tag>
                 Generate release notes relative to this tag instead of
                 gh's auto-detected previous release (passed through as
                 gh release create's --notes-start-tag).
  branch         Source branch to release from. Must not be "eng" - cut
                 releases from a version branch (e.g. 32.1.3).
  release_name   Release name, e.g. 32.1.3 (tag pushed will be v<release_name>).

Requirements:
  - gh CLI installed and authenticated (run 'gh auth login' once)
  - galaxy.yml's "version" field on <branch> must already match
    <release_name> (release.yaml publishes whatever version is in
    galaxy.yml, regardless of the release name/tag).

Example:
  ./create_release.sh --previous-tag v32.1.2 32.1.3 32.1.3
  ./create_release.sh --test 32.1.3 32.1.3
EOF
}

TEST_MODE=false
PREVIOUS_TAG=""
ARGS=()
while [ $# -gt 0 ]; do
    case "$1" in
        --test)
            TEST_MODE=true
            shift
            ;;
        --previous-tag)
            if [ $# -lt 2 ]; then
                echo "Error: --previous-tag requires a value."
                usage
                exit 1
            fi
            PREVIOUS_TAG="$2"
            shift 2
            ;;
        *)
            ARGS+=("$1")
            shift
            ;;
    esac
done
set -- "${ARGS[@]}"

if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    usage
    exit 0
fi

if [ $# -ne 2 ]; then
    usage
    exit 1
fi

if [ "$TEST_MODE" = true ]; then
    echo "Running in --test mode: release will be created as a draft (release.yaml will not fire), and the wait/watch step will be skipped."
fi

if ! command -v gh &>/dev/null; then
    echo "gh (GitHub CLI) not found. Install it: https://cli.github.com/ and run 'gh auth login'."
    exit 1
fi

if ! gh auth status &>/dev/null; then
    echo "gh CLI is not authenticated. Run 'gh auth login' first."
    exit 1
fi

BRANCH=$1
REL=$2
if [ "$BRANCH" = "eng" ]; then
    echo "Branch should not be ENG."
    exit 1
fi

if [ -z $REL ]; then
    echo "Pl. give the release version eg. 32.1.3"
    usage
    exit 1
fi

REL_TAG=v$REL
REL_TITLE=v$REL
echo "Release tag is $REL_TAG"

if git rev-parse -q --verify "refs/tags/$REL_TAG" >/dev/null || git ls-remote --exit-code --tags origin "$REL_TAG" >/dev/null 2>&1; then
    echo "Tag $REL_TAG already exists. Aborting to avoid overwriting an existing release tag."
    exit 1
fi

# release.yaml publishes whatever version is set in galaxy.yml, so make sure
# it matches the release being cut before tagging.
GALAXY_VERSION=$(git show "origin/$BRANCH:galaxy.yml" | sed -n 's/^version: *//p')
if [ "$GALAXY_VERSION" != "$REL" ]; then
    echo "Error: galaxy.yml version on origin/$BRANCH is '$GALAXY_VERSION', expected '$REL'."
    echo "Update galaxy.yml's version field on $BRANCH and push before running this script."
    exit 1
fi

git tag $REL_TAG origin/$BRANCH
git push origin $REL_TAG
set -e
git checkout -B $BRANCH origin/$BRANCH

# Creating the GitHub release is what triggers .github/workflows/release.yaml
# (on: release: published), which builds and publishes the collection to
# Ansible Galaxy.
RELEASE_CREATED_AT=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "Creating release $REL_TAG."
CREATE_ARGS=("$REL_TAG" --title "$REL_TITLE" --generate-notes)
if [ -n "$PREVIOUS_TAG" ]; then
    CREATE_ARGS+=(--notes-start-tag "$PREVIOUS_TAG")
fi
if [ "$TEST_MODE" = true ]; then
    CREATE_ARGS+=(--draft)
fi
gh release create "${CREATE_ARGS[@]}"

if [ "$TEST_MODE" = true ]; then
    echo "Test mode: skipping release.yaml wait/watch. Verify the draft with: gh release view $REL_TAG"
    exit 0
fi

# Find the workflow run that this release triggered, then wait for it to finish
# and fail this script if it fails.
echo "Waiting for the release.yaml workflow run to start..."
RUN_ID=""
for i in $(seq 1 30); do
    RUN_ID=$(gh run list --workflow=release.yaml --json databaseId,event,createdAt \
        --jq "[.[] | select(.event == \"release\" and .createdAt >= \"$RELEASE_CREATED_AT\")] | sort_by(.createdAt) | last | .databaseId // empty")
    if [ -n "$RUN_ID" ]; then
        break
    fi
    sleep 5
done

if [ -z "$RUN_ID" ]; then
    echo "Error: could not find the release.yaml run triggered by $REL_TAG. Check manually: gh run list --workflow=release.yaml"
    exit 1
fi

echo "Watching release.yaml run $RUN_ID..."
if gh run watch "$RUN_ID" --exit-status; then
    echo "release.yaml succeeded for $REL_TAG."
else
    echo "Error: release.yaml failed for $REL_TAG. See: gh run view $RUN_ID --log-failed"
    exit 1
fi
