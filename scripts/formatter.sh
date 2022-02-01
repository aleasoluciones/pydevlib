#!/bin/bash
#set -e

scripts_path="$1/scripts"
config_path="$1/config"
source $scripts_path/shared_utils/clean_pyc_files.sh
source $scripts_path/shared_utils/output.sh

echo
echo "----------------------------------------------------------------------"
echo "Running Black formatter on Python files"
echo "----------------------------------------------------------------------"
echo

if [ -z "$2" ]; then
    black .
else
    black $@
fi

info "Black formatting applied"
