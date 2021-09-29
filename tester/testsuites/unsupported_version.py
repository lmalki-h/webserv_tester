from http import HTTPStatus
from tester.httpserver.httpserver import * 
from tester.testsuites.response_format import *

def test_unsupported_http_version() -> str:

    """"https://datatracker.ietf.org/doc/html/rfc7230#section-2.6"""

    request = "GET /simplestindex.html HTTP/0.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.HTTP_VERSION_NOT_SUPPORTED)