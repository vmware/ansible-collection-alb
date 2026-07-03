#!/bin/bash
############################################################################
# ========================================================================
# Copyright (c) 2026 Broadcom Inc. and/or its subsidiaries. All Rights Reserved. Broadcom Confidential.
# ========================================================================
###

set -e
echo "Migrating avihost service files."
major_version=`cat /bootstrap/VERSION | grep Version | awk '{print $2}' | awk '{split($0,a,".");}{print a[1]}'`
BASEDIR=$(dirname "$0")

python_cmd='python3'
if [ $major_version -lt 20 ]
then
   echo "using python2"
   python_cmd="python"
fi

$python_cmd $BASEDIR/install.py

echo "Completed: Migration of avihost service files." 