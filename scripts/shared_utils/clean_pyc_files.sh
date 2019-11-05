#!/bin/bash

for pyc_file in $(find . -path *docker_data* -prune -o -name '*.pyc' -print); do
    rm $pyc_file
done
