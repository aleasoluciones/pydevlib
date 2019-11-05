#!/bin/bash

scripts_path=$1
config_path=$2
source $scripts_path/shared_utils/clean_pyc_files.sh

echo
echo "----------------------------------------------------------------------"
echo "Running YAPF formatter on Python files"
echo "----------------------------------------------------------------------"
echo

if [ -z "$3" ]; then
    yapf -r --style $config_path/.style.yapf .
else
    yapf -r --style $config_path/.style.yapf $3
fi
