#!/bin/bash

echo "HOLA"
clear
mamba -f documentation $1;

MAMBA_RETCODE=$?
exit $MAMBA_RETCODE
