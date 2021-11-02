#!/bin/bash

if [ -z "$VIRTUAL_ENV" ]; then
    echo "You need to be on a virtual environment to install dev dependencies"
else
    python -m pip install --upgrade pip wheel
    python -m pip install --upgrade -e .
fi
