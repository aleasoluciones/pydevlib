#!/bin/bash

source scripts/shared_utils/output.sh

echo
echo "----------------------------------------------------------------------"
echo "Copying git hooks"
echo "----------------------------------------------------------------------"
echo

echo "Current project: $(info $(basename $(pwd)))"
echo
for hook in config/git-hooks/*; do
  echo "--> Copying hook \"$(warning $(basename $hook))\""
  cp $hook .git/hooks/$(basename $hook)
done
echo
info "Every git hook was copied fine"
