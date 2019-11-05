#!/bin/bash
# Copy git hooks to your current git repository

echo
echo "----------------------------------------------------------------------"
echo "Copying git hooks"
echo "----------------------------------------------------------------------"
echo

echo "Current project: $(basename $(pwd))"
echo
for hook in config/git-hooks/*; do
  echo "--> Copying hook \"$(basename $hook)\""
  cp $hook .git/hooks/$(basename $hook)
done
echo
echo "Every git hook was copied fine"
