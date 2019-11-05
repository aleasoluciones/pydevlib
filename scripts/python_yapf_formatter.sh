#!/bin/bash

source scripts/shared_utils/clean_pyc_files.sh

echo
echo "----------------------------------------------------------------------"
echo "Running YAPF formatter on Python files"
echo "----------------------------------------------------------------------"
echo

if [ -z "$1" ]; then
    yapf -ir --style config/.style.yapf .
else
    yapf -ir --style config/.style.yapf $1
fi
