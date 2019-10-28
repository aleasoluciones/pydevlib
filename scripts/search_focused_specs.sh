#!/bin/bash

COLOR_FOR_BASH=\\e

if (( $(uname) == 'Darwin' )); then
    COLOR_FOR_BASH=\\x1B
fi

GREEN="$COLOR_FOR_BASH[32m"
RED="$COLOR_FOR_BASH[31m"
NO_COLOR='\033[0m' # No Color

function info(){
  echo -e "${GREEN}$1${NO_COLOR}"
}

function error(){
  echo -e "${RED}$1${NO_COLOR}"
}

echo
echo "----------------------------------------------------------------------"
echo "Searching for Focused Specs"
echo "----------------------------------------------------------------------"
echo
FOCUSED_SPECS=$(grep -rn --exclude-dir=dev --exclude=search_focused_specs.sh 'with fit\|with fcontext\|with fdescribe\|with fdescription' .)
if [ -z "$FOCUSED_SPECS" ]
then
    info "Focused specs NOT found"
    FOCUS_RETCODE=0
else
    error "Focused specs found:"
    echo
    echo "$FOCUSED_SPECS"
    FOCUS_RETCODE=1
fi

exit $FOCUS_RETCODE