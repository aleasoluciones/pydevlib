#!/bin/bash
#set -e

scripts_path="$1/scripts"
config_path="$1/config"
source $scripts_path/shared_utils/output.sh

echo
echo "----------------------------------------------------------------------"
echo "Copying git hooks"
echo "----------------------------------------------------------------------"
echo

echo "Current project: $(info $(basename $(pwd)))"
echo
for hook in $config_path/git-hooks/*; do
  echo "--> Copying hook \"$(warning $(basename $hook))\""
  cp $hook .git/hooks/$(basename $hook)
done
echo
info "Every git hook was copied fine"
