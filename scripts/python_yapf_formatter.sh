#!/bin/bash

for pyc_file in $(find . -path *docker_data* -prune -o -name '*.pyc' -print); do
    rm $pyc_file
done
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
