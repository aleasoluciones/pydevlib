import json
import datetime
import inspect
from pprint import pprint
from functools import wraps

from deepdiff import DeepDiff
from expects.matchers import Matcher


# Debugging utils
def printdiff(obj1, obj2):
    pprint(DeepDiff(obj1, obj2), indent=2)


# Custom expect matchers
class equal_json_dict(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, input_json):
        input_dict = json.loads(input_json)
        if input_dict == self._expected:
            return True, ["json contains the dict"]
        return False, ["json does not contain the dict"]


class be_datetime(Matcher):
    def __init__(self, format='%Y-%m-%d %H:%M:%S'):
        self._format = format

    def _match(self, subject):
        date_time_obj = datetime.datetime.strptime(subject, self._format)
        if date_time_obj:
            return True, ['date time found']
        return False, ['date time not found']


class have_decorator(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, function):
        decorators = self._get_method_decorators(function)
        if self._expected in decorators:
            return True, ['decorator found']
        return False, [f"{self._expected} decorator not found in {decorators}"]

    def _get_method_decorators(self, func):
        function_source = inspect.getsource(func)
        function_definition_index = function_source.find("def ")
        lines_before_definition = function_source[:function_definition_index].strip().splitlines()
        return [self._sanitize_decorator(line) for line in lines_before_definition if self._is_decorator_line(line)]

    def _is_decorator_line(self, line):
        return line.strip().startswith("@")

    def _sanitize_decorator(self, line):
        return line.strip().split()[0]


# Fake classes
class CallOrderAwareFake(object):
    class Decorators(object):
        @classmethod
        def call_order_aware(self, decorated_method):
            @wraps(decorated_method)
            def wrapper(self, *decorated_method_args, **decorated_method_kwargs):
                decorated_method(self, *decorated_method_args, **decorated_method_kwargs)
                decorated_method_name = decorated_method.__name__
                responses = self._responses[decorated_method_name]
                call_counter_for_response = self._call_counter[decorated_method_name]
                if len(responses) > call_counter_for_response:
                    response = responses[call_counter_for_response]
                    self._call_counter[decorated_method_name] += 1
                    if isinstance(response, Exception):
                        raise response
                    return response
                raise RuntimeError()

            return wrapper

    def __init__(self, responses):
        self._responses = responses
        self._call_counter = {}
        for method_name in responses.keys():
            self._call_counter[method_name] = 0


# Fake Class Implementantion Example
class FakeExample(CallOrderAwareFake):
    @CallOrderAwareFake.Decorators.call_order_aware
    def a_method(self, *args, **kwargs):
        pass