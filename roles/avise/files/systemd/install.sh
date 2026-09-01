#!/bin/sh

############################################################################
# ========================================================================
# Copyright (c) 2026 Broadcom Inc. and/or its subsidiaries. All Rights Reserved. Broadcom Confidential.
# ========================================================================
###

set -e

echo "Migrating avihost service files."

major_version=$(
    awk '/Version/ {
        split($2, a, ".");
        print a[1]
    }' /bootstrap/VERSION
)

BASEDIR=$(dirname "$0")

# install.py imports avi.* modules (available under the bundled Python 3.14).
# Prefer python3.14; fall back to python3 (or python for very old pre-20 releases)
# so the script still works on hosts with other python versions.
if command -v python3.14 >/dev/null 2>&1; then
   python_cmd='python3.14'
elif [ "$major_version" -lt 20 ]; then
   echo "using python2"
   python_cmd="python"
else
   python_cmd='python3'
fi

"$python_cmd" "$BASEDIR/install.py"

echo "Completed: Migration of avihost service files."