import logging
import base64

from tornado import escape
from tornado.testing import AsyncHTTPTestCase


class TornadoFunctionalTest(AsyncHTTPTestCase):
    API_USER_NAME = 'an_user'
    API_USER_PASSWORD = 'a_password'
    API_USER_NETWORKS = 'lab'

    def __init__(self,
                 auth_username=None,
                 auth_password=None,
                 debug=False,
                 application=None,
                 user_service=None,
                 **kwargs):
        super(TornadoFunctionalTest, self).__init__()

        self.auth_username = auth_username if auth_username else self.API_USER_NAME
        self.auth_password = auth_password if auth_password else self.API_USER_PASSWORD
        self.debug = debug
        self.application = application
        self.user_service = user_service
        self.extra_args = kwargs

    def _verbose_logger(self, value):
        # from https://stackoverflow.com/a/32437988
        logging.getLogger("tornado.access").disabled = not value

    def setUp(self):
        AsyncHTTPTestCase.setUp(self)
        self._user = self._add_user(
            username=self.auth_username,
            password=self.auth_password,
            networks=self.API_USER_NETWORKS)
        self._credentials = self._build_credentials(
            username=self.auth_username, password=self.auth_password)

    def tearDown(self):
        self._remove_user(self.auth_username)
        try:
            AsyncHTTPTestCase.tearDown(self)
        except Exception:
            pass

    def get_app(self):
        self.app = self.application.create(debug=self.debug, **self.extra_args)
        return self.app

    def _dump_when_error(self, response, verbose):
        if not verbose:
            return
        if response.error:
            fields = ["code", "error", "effective_url", "body"]
            for field in fields:
                print("{}: {}".format(field, getattr(response, field)))

    def fetch(self,
              url,
              method="GET",
              body=None,
              verbose=False,
              headers=None,
              allow_nonstandard_methods=False,
              **kwargs):
        self._verbose_logger(verbose)
        response = self._fetch_url(
            url,
            method=method,
            body=body,
            headers=headers,
            allow_nonstandard_methods=allow_nonstandard_methods)
        self._dump_when_error(response, verbose)
        return self._update_response_json_body(response)

    def _fetch_url(self, url, method, body, headers,
                   allow_nonstandard_methods):
        if not headers:
            headers = {}
        headers.update(self._json_headers())
        body = self._parse_to_json_if_dict(body)
        response = super(TornadoFunctionalTest, self).fetch(
            url,
            method=method,
            auth_username=self.auth_username,
            auth_password=self.auth_password,
            body=body,
            headers=headers,
            allow_nonstandard_methods=allow_nonstandard_methods)
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

    def _add_user(self, username, password, networks):
        self.user_service.add_user(
            username=username,
            password=password,
            networks=networks,
            local_admin=True)

    def _remove_user(self, username):
        self.user_service.remove_user(username)

    def _build_credentials(self, username, password):
        credentials = "{}:{}".format(username, password)
        encoded_credentials = base64.b64encode(credentials)
        return encoded_credentials

    def check_urls(self,
                   urls,
                   allowed_status_codes,
                   method='GET',
                   body=None,
                   network=API_USER_NETWORKS):
        for url in urls:
            endpoint = "/{}/{}".format(network, url)
            response = self.fetch(url=endpoint, method=method, body=body)
            self._handle_response(response, allowed_status_codes)

    def _handle_response(self, response, allowed_status_codes):
        if response.code < 300:
            return
        if response.code == 405 or response.code not in allowed_status_codes:
            error_text = "Response error url: {} code: {} error: {}".format(
                response.effective_url, response.code, response.error)
            print("Error", error_text)
            raise Exception(error_text)
