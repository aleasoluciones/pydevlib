#!/bin/bash
#set -e

scripts_path="$1/scripts"
source $scripts_path/shared_utils/clean_pyc_files.sh

SPEC_PATTERN="regression_specs"
SEARCH_PATH="."
IGNORE_PATH="systems"
SPEC_FILES=$(find $SEARCH_PATH -maxdepth 2 -type d -name $SPEC_PATTERN | grep -v $IGNORE_PATH)
SPEC_FILES_RETCODE=$?

if [ $SPEC_FILES_RETCODE = 1 ]; then
    exit
fi


echo
echo "----------------------------------------------------------------------"
echo "Running Regression Specs"
echo "----------------------------------------------------------------------"
echo


if [ -z "$2"  ]; then
    FORMATTER="progress"
    mamba -f $FORMATTER $SPEC_FILES --enable-coverage;
elif [ $2 = "doc" ]; then
    FORMATTER="documentation"
    mamba -f $FORMATTER $SPEC_FILES --enable-coverage;
elif [ $2 = "debug" ]; then
    for f in $SPEC_FILES; do
        echo "$f ..."
        mamba $f --enable-coverage
    done;
fi

MAMBA_RETCODE=$?

exit $MAMBA_RETCODE
