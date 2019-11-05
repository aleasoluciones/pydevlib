#!/bin/bash

scripts_path=$1
source $scripts_path/shared_utils/clean_pyc_files.sh

echo
echo "----------------------------------------------------------------------"
echo "Running Factory tests"
echo "----------------------------------------------------------------------"
echo

python $scripts_path/../infdev/run_factory_tests.py
