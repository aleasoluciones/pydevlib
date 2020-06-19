#!/bin/bash
#set -e

scripts_path="$1/scripts"
source $scripts_path/shared_utils/clean_pyc_files.sh

echo
echo "----------------------------------------------------------------------"
echo "Running Factory tests"
echo "----------------------------------------------------------------------"
echo

python $1/pydevlib/factory_tests.py
