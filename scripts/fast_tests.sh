#!/bin/bash
#set -e

unit_tests &&\
integration_tests &&\
regression_tests &&\
factory_tests
