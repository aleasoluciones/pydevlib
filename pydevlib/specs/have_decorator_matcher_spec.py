from functools import wraps

from mamba import description, context, it
from expects import expect
from expects.matchers import Matcher

from pydevlib.spec_helpers import have_decorator


def dummy_decorator(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func

@dummy_decorator
def function_with_decorator():
    pass

def function_without_decorator():
    pass

@dummy_decorator # <-- this is the decorator
# dummy comment
def function_with_decorator_and_comments():
    pass


DUMMY_DECORATOR_AS_STR = "@dummy_decorator"


with description("'have decorator' matcher specs"):
    with context("FEATURE: positive assertion"):
        with context("when function has the decorator"):
            with it("passes"):
                expect(function_with_decorator).to(have_decorator(DUMMY_DECORATOR_AS_STR))

        with context("when function DOES NOT have the decorator"):
            with it("fails"):
                try:
                    expect(function_without_decorator).to(have_decorator(DUMMY_DECORATOR_AS_STR))
                except AssertionError:
                    pass

    with context("FEATURE: negative assertion"):
        with context("when function does not have the decorator"):
            with it("passes"):
                expect(function_without_decorator).not_to(have_decorator(DUMMY_DECORATOR_AS_STR))

        with context("when function DO HAS the decorator"):
            with it("fails"):
                try:
                    expect(function_with_decorator).not_to(have_decorator(DUMMY_DECORATOR_AS_STR))
                except AssertionError:
                    pass

    with context("managing comments"):
        with it("ignores comments"):
            expect(function_with_decorator_and_comments).to(have_decorator(DUMMY_DECORATOR_AS_STR))
                    