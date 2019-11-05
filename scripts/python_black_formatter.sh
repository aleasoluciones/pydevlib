#!/bin/bash

source scripts/shared_utils/clean_pyc_files.sh

echo
echo "----------------------------------------------------------------------"
echo "Running BLACK formatter on Python files"
echo "----------------------------------------------------------------------"
echo

if [ -z "$1" ]; then
    black -t py37 .
else
    black -t py37 $1
fi

