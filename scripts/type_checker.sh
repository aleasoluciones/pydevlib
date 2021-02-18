#!/bin/bash
#set -e

scripts_path="$1/scripts"
config_path="$1/config"
source $scripts_path/shared_utils/clean_pyc_files.sh

SEARCH_PATH="."

echo
echo "----------------------------------------------------------------------"
echo "Type checking the codebase"
echo "----------------------------------------------------------------------"
echo

mypy $SEARCH_PATH --config-file $config_path/mypy.ini

MYPY_RETCODE=$?

exit $MYPY_RETCODE