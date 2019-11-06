#!/bin/bash

scripts_path="$1/scripts"
config_path="$1/config"
source $scripts_path/shared_utils/clean_pyc_files.sh

echo
echo "----------------------------------------------------------------------"
echo "Running YAPF formatter on Python files"
echo "----------------------------------------------------------------------"
echo

if [ -z "$2" ]; then
    yapf -ir --style $config_path/.style.yapf .
else
    yapf -ir --style $config_path/.style.yapf $@
fi
