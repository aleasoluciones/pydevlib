#!/usr/bin/env python

from subprocess import call
import argparse
import traceback


SCRIPT_TYPES_PATH = {
    'git_hooks': "tools/configure_git_hooks.sh",
    'linter': "scripts/python_linter.sh",
    'formatter': "scripts/python_formatter.sh",
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
    parser.add_argument('-t', '--type', action='store', required=False, help='Script type')
    parser.add_argument('-l', '--list', action='store_true', required=False, help=' List dev script types')
    args = parser.parse_args()
    if args.type:
        script_type = SCRIPT_TYPES_PATH[args.type]
        call(script_type)
    if args.list:
        for script_type in SCRIPT_TYPES_PATH.keys():
            print(script_type)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(traceback.print_exc())
