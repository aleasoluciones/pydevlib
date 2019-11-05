#!/usr/bin/env python

from subprocess import call
import argparse
import traceback


SCRIPT_TYPES_PATH = {
    'git_hooks': "scripts/git_hooks.sh",
    'linter': "scripts/python_linter.sh",
    'yapf_formatter': "scripts/python_yapf_formatter.sh",
    'black_formatter': "scripts/python_black_formatter.sh",
    'search_focused_specs': "scripts/search_focused_specs.sh",
    'unit_tests': "scripts/unit_tests.sh",
    'factory_tests': "scripts/factory_tests.sh",
    'integration_tests': "scripts/integration_tests.sh",
    'functional_tests': "scripts/functional_tests.sh",
    'acceptance_tests': "scripts/acceptance_tests.sh",
    'all_local_tests': "scripts/all_local_tests.sh",
    'all_tests': "scripts/all_tests.sh",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--run', action='store', required=False, help='Run script')
    parser.add_argument('-l', '--list', action='store_true', required=False, help=' List dev script types')
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


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(traceback.print_exc())
