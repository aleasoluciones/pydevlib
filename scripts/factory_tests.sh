#!/bin/bash

scripts_path="$1/scripts"
source $scripts_path/shared_utils/clean_pyc_files.sh

echo
echo "----------------------------------------------------------------------"
echo "Running Factory tests"
echo "----------------------------------------------------------------------"
echo

python $1/infdev/factory_tests.py
