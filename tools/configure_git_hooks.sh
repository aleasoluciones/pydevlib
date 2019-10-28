#!/bin/bash
# Copy git hooks to your current git repository

echo
echo "----------------------------------------------------------------------"
echo "Copying git hooks"
echo "----------------------------------------------------------------------"
echo

current_project=$(basename $(pwd))

echo "Current project: $current_project"
for hook in tools/git-hooks/*; do
  echo "--> Copying hook \"$(basename $hook)\""
  cp $hook /tmp
  sed -i -e "s/current_project/$current_project/" /tmp/$(basename $hook)
  cp /tmp/$(basename $hook) .git/hooks/$(basename $hook)
done
echo "Every git hook was copied fine"
