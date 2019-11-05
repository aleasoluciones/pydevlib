#!/usr/bin/env python

from subprocess import call
import argparse
import traceback
import os

current_file_path = os.path.dirname(os.path.abspath(__file__))
scripts_path = f"{current_file_path}/../scripts"

SCRIPT_TYPES_PATH = {
    "git_hooks": f"{scripts_path}/git_hooks.sh",
    "linter": f"{scripts_path}/python_linter.sh",
    "yapf_formatter": f"{scripts_path}/python_yapf_formatter.sh",
    "black_formatter": f"{scripts_path}/python_black_formatter.sh",
    "focused_specs": f"{scripts_path}/search_focused_specs.sh",
    "unit_tests": f"{scripts_path}/unit_tests.sh",
    "factory_tests": f"{scripts_path}/factory_tests.sh",
    "integration_tests": f"{scripts_path}/integration_tests.sh",
    "functional_tests": f"{scripts_path}/functional_tests.sh",
    "acceptance_tests": f"{scripts_path}/acceptance_tests.sh",
    "local_tests": f"{scripts_path}/local_tests.sh",
    "all_tests": f"{scripts_path}/all_tests.sh",
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
        help=" List dev script types",
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
        call([script_type, *unknown_args[1:]])
    except KeyError:
        print("There's no such script to run :( The available scripts list is:\n")
        for script_type in SCRIPT_TYPES_PATH.keys():
            print(f"- {script_type}")
        print("")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        print(traceback.print_exc())
