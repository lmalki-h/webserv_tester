from http import HTTPStatus
from tester.httpserver.httpserver import * 
from tester.testsuites.response_format import *
from config import *

def test_max_uri_length() -> str:
    uri = "/" + "a" * (config.MAX_URI_LENGTH - 1)
    request = "GET {} HTTP/1.1\r\nHost: LOL\r\n\r\n".format(uri)
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.REQUEST_URI_TOO_LONG)
