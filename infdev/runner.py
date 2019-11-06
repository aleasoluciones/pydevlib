#!/usr/bin/env python

import os
import argparse
import traceback
from subprocess import call

CURRENT_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_PATH = f"{CURRENT_FILE_PATH}/../scripts"
CONFIG_PATH = f"{CURRENT_FILE_PATH}/../config"

SCRIPT_TYPES_PATH = {
    "git_hooks": f"{SCRIPTS_PATH}/git_hooks.sh",
    "linter": f"{SCRIPTS_PATH}/python_linter.sh",
    "yapf_formatter": f"{SCRIPTS_PATH}/yapf_formatter.sh",
    "black_formatter": f"{SCRIPTS_PATH}/black_formatter.sh",
    "focused_specs": f"{SCRIPTS_PATH}/focused_specs.sh",
    "unit_tests": f"{SCRIPTS_PATH}/unit_tests.sh",
    "factory_tests": f"{SCRIPTS_PATH}/factory_tests.sh",
    "integration_tests": f"{SCRIPTS_PATH}/integration_tests.sh",
    "functional_tests": f"{SCRIPTS_PATH}/functional_tests.sh",
    "acceptance_tests": f"{SCRIPTS_PATH}/acceptance_tests.sh",
    "local_tests": f"{SCRIPTS_PATH}/local_tests.sh",
    "all_tests": f"{SCRIPTS_PATH}/all_tests.sh",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r", "--run", action="store", required=False, help="Run script"
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        required=False,
        help="List dev script types",
    )
    args, unknown_args = parser.parse_known_args()

    if args.list:
        print("The available scripts list is:\n")
        for script_type in SCRIPT_TYPES_PATH.keys():
            print(f"- {script_type}")
        print("")
        return

    if not args.run and unknown_args:
        args.run = unknown_args[0]

    try:
        script_type = SCRIPT_TYPES_PATH[args.run]
        exit(call([script_type, SCRIPTS_PATH, CONFIG_PATH, *unknown_args[1:]]))
    except KeyError:
        print("There's no such script to run :( The available scripts list is:\n")
        for script_type in SCRIPT_TYPES_PATH.keys():
            print(f"- {script_type}")
        print("")


def mambo():
    parser = argparse.ArgumentParser()
    args, unknown_args = parser.parse_known_args()
    script_type = f"{SCRIPTS_PATH}/mambo.sh"
    try:
        exit(call([script_type, *unknown_args[1:]]))
    except Exception:
        print(traceback.print_exc())
        exit(1)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(traceback.print_exc())
        exit(1)
