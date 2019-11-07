#!/bin/bash
#set -e

scripts_path="$1/scripts"
config_path="$1/config"
source $scripts_path/shared_utils/output.sh

echo
echo "----------------------------------------------------------------------"
echo "Running Python linter: pylint"
echo "----------------------------------------------------------------------"
echo

EXIT_CODE=0

if [ -z "$2"  ]; then
    files=$(find . -type f -name "*.py" | grep -v 'spec')
    if [[ $files ]]; then
        info "Analizing PRODUCTION code..."

        output=$(pylint --rcfile $config_path/.pylintrc ${files})
        retcode=$?
        exit_on_fatal_or_error $retcode "$output"
    else
        warning 'Not found python PRODUCTION code'
        echo
    fi

    spec_files=$(find . -type f -name "*spec.py")
    if [[ $spec_files ]]; then
      info "Analizing SPECS code..."
      output=$(pylint --rcfile $config_path/.pylintrc-mamba ${spec_files})
      retcode=$?
      exit_on_fatal_or_error $retcode "$output"
    else
        warning 'Not found python SPECS code'
        echo
    fi

elif [ $2 = "staged" ]; then
  # https://git-scm.com/docs/git-status#_output
  # M = modified A = added D = deleted R = renamed C = copied U = updated but unmerged
  staged_files=$(git status --porcelain | grep "^[MCA]" | awk '$1~/^[MCA]/ && $2~/.py$/ {print $2}')

  if [[ $staged_files ]]; then
        source_files=$(echo $staged_files | grep -v 'spec')
        if [[ $source_files ]]; then
          info 'Analizing git staged PRODUCTION code...'
          output=$(pylint --rcfile $config_path/.pylintrc $source_files)
          retcode=$?
          exit_on_fatal_or_error $retcode "$output"
        fi ;

        spec_files=$(echo $staged_files | grep 'spec')
        if [[ $spec_files ]]; then
          info "Analizing git staged SPECS code..."
          output=$(pylint --rcfile $config_path/.pylintrc-mamba ${spec_files})
          retcode=$?
          exit_on_fatal_or_error $retcode "$output"
        fi

    else
        warning 'Not found python staged files'
        echo
    fi
fi

exit $EXIT_CODE
