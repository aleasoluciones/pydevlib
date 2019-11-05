#!/bin/bash

scripts_path=$1
source $scripts_path/shared_utils/clean_pyc_files.sh

echo
echo "----------------------------------------------------------------------"
echo "Running Integration Specs"
echo "----------------------------------------------------------------------"
echo

SPEC_PATTERN="integration_specs"
SEARCH_PATH="."
IGNORE_PATH="systems"
SPEC_FILES=$(find $SEARCH_PATH -maxdepth 2 -type d -name $SPEC_PATTERN | grep -v $IGNORE_PATH)

if [ -z "$3"  ]; then
    FORMATTER="progress"
    mamba -f $FORMATTER $SPEC_FILES;
elif [ $3 = "doc" ]; then
    FORMATTER="documentation"
    mamba -f $FORMATTER $SPEC_FILES;
elif [ $3 = "debug" ]; then
    for f in $SPEC_FILES; do
        echo "$f ..."
        mamba $f
    done;
fi

MAMBA_RETCODE=$?

exit $MAMBA_RETCODE
