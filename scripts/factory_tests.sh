#!/bin/bash

source scripts/shared_utils/clean_pyc_files.sh

echo
echo "----------------------------------------------------------------------"
echo "Running Factory tests"
echo "----------------------------------------------------------------------"
echo

python infdev/run_factory_tests.py