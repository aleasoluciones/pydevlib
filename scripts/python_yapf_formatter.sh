#!/bin/bash

source scripts/shared_utils/clean_pyc_files.sh

echo
echo "----------------------------------------------------------------------"
echo "Running YAPF formatter on Python files"
echo "----------------------------------------------------------------------"
echo

if [ -z "$1" ]; then
    yapf -ir .
else
    yapf -ir $1
fi
