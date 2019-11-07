#!/bin/bash
#set -e

unit_tests &&\
integration_tests &&\
factory_tests &&\
functional_tests
