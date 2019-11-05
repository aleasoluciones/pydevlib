#!/bin/bash

scripts_path=$1
source $scripts_path/shared_utils/output.sh

echo
echo "----------------------------------------------------------------------"
echo "Searching for Focused Specs"
echo "----------------------------------------------------------------------"
echo

FOCUSED_SPECS=$(grep -rn --exclude-dir={$scripts_path,scripts} --exclude=search_focused_specs.sh 'with fit\|with fcontext\|with fdescribe\|with fdescription' .)
if [ -z "$FOCUSED_SPECS" ]; then
    info "Focused specs NOT found"
    FOCUS_RETCODE=0
else
    error "Focused specs found:"
    echo
    echo "$FOCUSED_SPECS"
    FOCUS_RETCODE=1
fi

exit $FOCUS_RETCODE
