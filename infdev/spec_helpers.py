from functools import wraps
from deepdiff import DeepDiff


def printdiff(obj1, obj2):
    print(DeepDiff(obj1, obj2))


class CallOrderAwareFake(object):
    class Decorators(object):
        @classmethod
        def call_order_aware(self, decorated_method):
            @wraps(decorated_method)
            def wrapper(self, *decorated_method_args, **decorated_method_kwargs):
                decorated_method(
                    self, *decorated_method_args, **decorated_method_kwargs
                )
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


class FakeExample(CallOrderAwareFake):
    @CallOrderAwareFake.Decorators.call_order_aware
    def a_method(self, *args, **kwargs):
        pass
