#!/bin/bash

if [ -z "$VIRTUAL_ENV" ]; then
    echo "You need to be on a virtual environment to install dev dependencies"
else
    python -m pip install --upgrade pip wheel setuptools

    if [ -e requirements-versioned.txt ]; then
        python -m pip install --upgrade -r requirements-versioned.txt
    fi
    if [ -e requirements-git.txt ]; then
        python -m pip install --upgrade -r requirements-git.txt
    fi
    if [ -e requirements-dev.txt ]; then
        python -m pip install --upgrade -r requirements-dev.txt
    fi
    if [ -e requirements.txt ]; then
        python -m pip install --upgrade -r requirements.txt
    fi

    python -m pip install --upgrade -e .

    for package in $(ls -d */); do pushd $package; if [ -e setup.py ]; then python -m pip install --upgrade -e .; fi; popd; done
fi

git_hooks
