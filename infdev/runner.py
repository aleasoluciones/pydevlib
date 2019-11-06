#!/usr/bin/env python

import sys
import os
import argparse
import traceback
from subprocess import call

MODULE_BASE_PATH = f"{os.path.dirname(os.path.abspath(__file__))}/.."
COMMANDS = [
    "git_hooks",
    "linter",
    "yapf_formatter",
    "black_formatter",
    "focused_specs",
    "unit_tests",
    "factory_tests",
    "integration_tests",
    "functional_tests",
    "acceptance_tests",
    "local_tests",
    "all_tests",
]


def run(script_name, without_paths=False):
    # pylint: disable=broad-except
    parser = argparse.ArgumentParser()
    _, unknown_args = parser.parse_known_args()
    script_type = f"{MODULE_BASE_PATH}/scripts/{script_name}.sh"
    try:
        if without_paths:
            sys.exit(call([script_type, *unknown_args[1:]]))
        else:
            sys.exit(call([script_type, MODULE_BASE_PATH, *unknown_args[1:]]))
    except Exception:
        print(traceback.print_exc())
        sys.exit(1)


def infdev():
    print("The available commands list is:\n")
    for command in COMMANDS:
        print(f"- {command}")
    print("")


def mambo():
    run(mambo.__name__, without_paths=True)


def git_hooks():
    run(git_hooks.__name__)


def linter():
    run(linter.__name__)


def yapf_formatter():
    run(yapf_formatter.__name__)


def black_formatter():
    run(black_formatter.__name__)


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


def local_tests():
    run(local_tests.__name__)


def all_tests():
    run(all_tests.__name__)


if __name__ == "__main__":
    # pylint: disable=broad-except
    try:
        infdev()
    except Exception:
        print(traceback.print_exc())
        sys.exit(1)
