#!/bin/bash
#set -e

clear
mamba -f documentation $@;

MAMBA_RETCODE=$?
exit $MAMBA_RETCODE
