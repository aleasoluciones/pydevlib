#!/bin/bash

if [ -z "$VIRTUAL_ENV" ]; then
    echo "You need to be on a virtual environment to install dev dependencies"
    :
else
    echo
    echo "----------------------------------------------------------------------"
    echo "Installing Dev Dependencies"
    echo "----------------------------------------------------------------------"
    echo
    python setup.py develop
fi
