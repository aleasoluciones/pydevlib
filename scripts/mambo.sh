#!/bin/bash

clear
mamba -f documentation $1;

MAMBA_RETCODE=$?
exit $MAMBA_RETCODE
