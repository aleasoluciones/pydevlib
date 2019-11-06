#!/bin/bash

scripts_path="$1/scripts"
source $scripts_path/shared_utils/clean_pyc_files.sh

echo
echo "----------------------------------------------------------------------"
echo "Running BLACK formatter on Python files"
echo "----------------------------------------------------------------------"
echo

if [ -z "$2" ]; then
    black -t py37 .
else
    black -t py37 $@
fi
