#!/bin/bash

install_dependencies () {
    if [ -e $1 ]; then
        echo "Installing $1 dependencies"
        python -m pip install --use-pep517 --upgrade -r $1
    fi
}

if [ -z "$VIRTUAL_ENV" ]; then
    echo "You need to be on a virtual environment to install dev dependencies"
else
    python -m pip install --upgrade pip wheel setuptools

    install_dependencies requirements-versioned.txt
    install_dependencies requirements-git.txt
    install_dependencies requirements-dev.txt
    install_dependencies requirements.txt

    echo "Installing local package"
    if [ -e setup.py ]; then
        python -m pip install --use-pep517 --upgrade -e .
    fi

    echo "Installing modules"
    for package in $(ls -d */); do pushd $package; if [ -e setup.py ]; then python -m pip install --use-pep517 --upgrade -e .; fi; popd; done

    git_hooks
fi
