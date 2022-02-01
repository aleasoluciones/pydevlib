#!/usr/bin/env python

import sys
import os
import argparse
import traceback
from subprocess import call

MODULE_BASE_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/.."
COMMANDS = [
    "mambo -> Alias for mamba -f documentation",
    "git_hooks -> Install pre-commit and pre-push git hooks",
    "linter -> Run pylint for production and specs code",
    "type_checker -> Run MyPY for production and specs code to perform static type checking",
    "formatter -> Run Black to format python code",
    "focused_specs -> Search focused specs across the code",
    "unit_tests -> Run unit tests",
    "factory_tests -> Run factory tests",
    "integration_tests -> Run integration tests",
    "regression_tests -> Run regression tests",
    "functional_tests -> Run functional tests",
    "acceptance_tests -> Run acceptance tests",
    "fast_tests -> Run all fast tests (unit, factory and integration tests)",
    "all_tests -> Run all tests but acceptance tests (unit, factory, integration and functional tests",
]


def run(script_name, without_paths=False):
    # pylint: disable=broad-except
    parser = argparse.ArgumentParser()
    _, unknown_args = parser.parse_known_args()
    script_type = f"{MODULE_BASE_PATH}/scripts/{script_name}.sh"
    try:
        if without_paths:
            sys.exit(call([script_type, *unknown_args]))
        else:
            sys.exit(call([script_type, MODULE_BASE_PATH, *unknown_args]))
    except Exception:
        print(traceback.print_exc())
        sys.exit(1)


def pydevlib():
    print("The available commands list is:\n")
    for index, command in enumerate(COMMANDS):
        print(f"{index + 1}) {command}")
    print("")


def mambo():
    run(mambo.__name__, without_paths=True)


def git_hooks():
    run(git_hooks.__name__)


def linter():
    run(linter.__name__)


def type_checker():
    run(type_checker.__name__)


def formatter():
    run(formatter.__name__)


def focused_specs():
    run(focused_specs.__name__)


def unit_tests():
    run(unit_tests.__name__)


def factory_tests():
    run(factory_tests.__name__)


def integration_tests():
    run(integration_tests.__name__)


def functional_tests():
    run(functional_tests.__name__)


def acceptance_tests():
    run(acceptance_tests.__name__)


def regression_tests():
    run(regression_tests.__name__)


def fast_tests():
    run(fast_tests.__name__)


def all_tests():
    run(all_tests.__name__)


if __name__ == "__main__":
    # pylint: disable=broad-except
    try:
        pydevlib()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
