#!/bin/bash

for pyc_file in $(find . -path *docker_data* -prune -o -name '*.pyc' -print); do
    rm $pyc_file
done

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

