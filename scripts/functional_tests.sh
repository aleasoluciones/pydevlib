#!/bin/bash

scripts_path="$1/scripts"
source $scripts_path/shared_utils/clean_pyc_files.sh

echo
echo "----------------------------------------------------------------------"
echo "Running Functional Specs"
echo "----------------------------------------------------------------------"
echo

SPEC_PATTERN="functional_specs"
SEARCH_PATH="."
IGNORE_PATH="systems"
SPEC_FILES=$(find $SEARCH_PATH -maxdepth 2 -type d -name $SPEC_PATTERN | grep -v $IGNORE_PATH)

if [ -z "$2"  ]; then
    FORMATTER="progress"
    mamba -f $FORMATTER $SPEC_FILES;
elif [ $2 = "doc" ]; then
    FORMATTER="documentation"
    mamba -f $FORMATTER $SPEC_FILES;
elif [ $2 = "debug" ]; then
    for f in $SPEC_FILES; do
        echo "$f ..."
        mamba $f
    done;
fi

MAMBA_RETCODE=$?

exit $MAMBA_RETCODE
