import logging
import traceback

from tornado import escape
from tornado.testing import AsyncHTTPTestCase


class TornadoFunctionalTest(AsyncHTTPTestCase):
    def __init__(self, application, debug=False, **kwargs):
        super(TornadoFunctionalTest, self).__init__()

        self.application = application
        self.debug = debug
        self.extra_args = kwargs

    def _verbose_logger(self, value):
        # from https://stackoverflow.com/a/32437988
        logging.getLogger("tornado.access").disabled = not value

    def setUp(self):
        try:
            self._verbose_logger(self.debug)
            AsyncHTTPTestCase.setUp(self)
        except Exception as exc:
            traceback.print_tb(exc.__traceback__)
            print("Exception", str(exc))
            exit(1)

    def tearDown(self):
        AsyncHTTPTestCase.tearDown(self)

    def get_app(self):
        self.app = self.application.create(debug=self.debug, **self.extra_args)
        return self.app

    def _dump_when_error(self, response, verbose):
        if not verbose:
            return
        if response.error:
            fields = ["code", "error", "effective_url", "body"]
            for field in fields:
                print(f"{field}: {getattr(response, field)}")

    def fetch(
        self,
        url,
        method="GET",
        body=None,
        verbose=False,
        headers=None,
        allow_nonstandard_methods=False,
        **kwargs,
    ):
        auth = kwargs.get("auth", None)
        if not auth:
            auth = self.extra_args.get("auth", None)
        self._verbose_logger(verbose)
        response = self._fetch_url(
            url,
            method=method,
            auth=auth,
            body=body,
            headers=headers,
            allow_nonstandard_methods=allow_nonstandard_methods,
        )
        self._dump_when_error(response, verbose)
        return self._update_response_json_body(response)

    def _fetch_url(self, url, method, auth, body, headers, allow_nonstandard_methods):
        if not headers:
            headers = {}
        headers.update(self._json_headers())
        body = self._parse_to_json_if_dict(body)
        fetch_options = {
            "path": url,
            "method": method,
            "body": body,
            "headers": headers,
            "allow_nonstandard_methods": allow_nonstandard_methods,
        }
        if auth:
            fetch_options.update({
                "auth_username": auth[0],
                "auth_password": auth[1],
            })

        response = super(TornadoFunctionalTest, self).fetch(**fetch_options)
        return response

    def _json_headers(self):
        return {"Content-type": "application/json"}

    def _parse_to_json_if_dict(self, body):
        if isinstance(body, dict):
            return escape.json_encode(body)
        return body

    def _update_response_json_body(self, response):
        # Warning: mutation
        response.json_body = None
        try:
            if response.body:
                response.json_body = escape.json_decode(response.body.decode())
        except ValueError:
            # do nothing, only pass error, json_body is none
            pass

        return response

    def runTest(self):
        pass
