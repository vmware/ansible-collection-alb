#!/bin/sh

############################################################################
# ========================================================================
# Copyright (c) 2026 Broadcom Inc. and/or its subsidiaries. All Rights Reserved. Broadcom Confidential.
# ========================================================================
###

set -e

echo "Migrating avihost service files."

BASEDIR=$(dirname "$0")

# Minimum supported SE version is 30.x (Python 3 only); legacy pre-20 Python 2 check removed.
python3 "$BASEDIR/install.py"

echo "Completed: Migration of avihost service files."