#!/bin/bash

if [ -z "$VIRTUAL_ENV" ]; then
    echo "You need to be on a virtual environment to install dev dependencies"
else
    echo
    echo "----------------------------------------------------------------------"
    echo "Installing Dev Dependencies"
    echo "----------------------------------------------------------------------"
    echo
    python setup.py develop
    for package in $(ls -d */); do pushd $package; if [ -e setup.py ]; then python setup.py develop; fi; popd; done
    pip install pip --upgrade
    if [ -e requirements.txt ]; then
        pip install -r requirements.txt --upgrade
    fi
    if [ -e requirements-dev.txt ]; then
        pip install -r requirements-dev.txt --upgrade
    fi
fi