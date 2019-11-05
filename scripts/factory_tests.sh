#!/bin/bash

for pyc_file in $(find . -path *docker_data* -prune -o -name '*.pyc' -print); do
    rm $pyc_file
done

echo
echo "----------------------------------------------------------------------"
echo "Running Factory tests"
echo "----------------------------------------------------------------------"
echo

python infdev/run_factory_tests.py