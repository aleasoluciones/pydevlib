#!/bin/bash

COLOR_FOR_BASH=\\e

if [[ $(uname) == 'Darwin' ]]; then
    COLOR_FOR_BASH=\\x1B
fi

GREEN="$COLOR_FOR_BASH[32m"
YELLOW="$COLOR_FOR_BASH[33m"
RED="$COLOR_FOR_BASH[31m"
NO_COLOR='\033[0m' # No Color

function info(){
  echo -e "${GREEN}$1${NO_COLOR}"
}

function warning(){
  echo -e "${YELLOW}$1${NO_COLOR}"
}

function error(){
  echo -e "${RED}$1${NO_COLOR}"
}

function force_exit(){
    exit_code=$1
    echo "Exit code:" $exit_code
    exit $exit_code
}

function exit_on_fatal_or_error(){
  FATAL_MESSAGE_ISSUED=1
  ERROR_MESSAGE_ISSUED=2
  retcode=$1
  output=$2
  is_fatal=$(($retcode & $FATAL_MESSAGE_ISSUED))
  is_error=$(($retcode & $ERROR_MESSAGE_ISSUED))
  undescartable_error=$(( $is_fatal || $is_error ))

  if [ "$undescartable_error" -ne "0" ]; then
    EXIT_CODE=$(($EXIT_CODE || $undescartable_error))
    error "Error de linter: ${retcode}"
    error "fatal and errors: "
    fatals_and_errors=$(echo "$output" | grep -E "[EF][0-9]{4}")
    echo "${fatals_and_errors}"
    force_exit $EXIT_CODE
  fi

  echo "$output"
  echo
}
