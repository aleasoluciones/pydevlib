import sys
import types
import importlib
import traceback
import os
import fnmatch
import re
from datetime import datetime

TOTAL_TESTS_PASSED = 0
LAST_CALL = None
GREEN_COLOR = "\033[0;32m"
WHITE_COLOR = "\033[0;39m"
RED_COLOR = "\033[91m"


def find_and_call_functions_from():
    # pylint: disable=global-statement
    global TOTAL_TESTS_PASSED
    global LAST_CALL

    factories = []
    current_working_directory = os.getcwd()

    for root, _, filenames in os.walk(current_working_directory):
        for filename in fnmatch.filter(filenames, "*factory.py"):
            factory_relative_path = f".{os.path.join(root, filename).replace(current_working_directory, '')}"
            if ("src" not in factory_relative_path and "build" not in factory_relative_path):
                factories.append(factory_relative_path)

    initial_time = datetime.utcnow()

    for factory_file in factories:
        a_factory = _import_module(factory_file)
        for element_name in dir(a_factory):
            element = getattr(a_factory, element_name)

            if callable(element):
                if isinstance(element, types.FunctionType) and not element_name.startswith("__"):
                    LAST_CALL = f"===> Exception in Factory file: {factory_file} Testing to call: {element_name}"
                    _check_function_arguments_and_call(element)

                    # ----------------------------------
                    TOTAL_TESTS_PASSED += 1
                    sys.stdout.write(GREEN_COLOR)
                    sys.stdout.write(".")
                    sys.stdout.write(WHITE_COLOR)

    elapsed_time = datetime.utcnow() - initial_time
    print(f"\n{GREEN_COLOR}")
    print(f"{TOTAL_TESTS_PASSED} examples ran in {elapsed_time.total_seconds():.4f} seconds{WHITE_COLOR}")


def _check_function_arguments_and_call(element):
    # ----------------------------------------------
    # Check if functions has none optional arguments
    # ----------------------------------------------
    number_of_arguments = element.__code__.co_argcount
    all_arguments_and_local_variables_names = element.__code__.co_varnames
    arguments_with_default_value = element.__defaults__ if element.__defaults__ else []
    if arguments_with_default_value is not None or arguments:
        required_arguments = all_arguments_and_local_variables_names[:number_of_arguments - len(arguments_with_default_value)]
        if required_arguments:
            element(**{required_argument: "irrelevant_argument_value" for required_argument in required_arguments})
        else:
            element()
    else:
        element()


def _import_module(module_name):
    # pylint: disable=broad-except
    try:
        file_to_import = (re.sub(r"\./.+?/", "", module_name).replace("/", ".").replace(".py", ""))
        return importlib.import_module(file_to_import)
    except Exception:
        file_to_import = (re.sub(r"\./", "", module_name).replace("/", ".").replace(".py", ""))
        return importlib.import_module(file_to_import)
    # https://stackoverflow.com/questions/4821104/python-dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported


if __name__ == "__main__":
    # pylint: disable=broad-except
    try:
        find_and_call_functions_from()
        sys.exit(0)
    except Exception as exc:
        print(f"\n{RED_COLOR}")
        print(f"{LAST_CALL} -> {exc}\n")
        traceback.print_exc()
        print(f"{WHITE_COLOR}\n")
        sys.exit(1)
