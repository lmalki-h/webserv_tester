# TODO: test date is in RFC recommended format
# test http version
# test content-length matches body size
# test mime type

from http import HTTPStatus
from tester.httpserver.httpserver import * 

def test_unsupported_http_version() -> str:
    request = "GET / HTTP/0.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    # request = make_request("unsupported_http_version.http", "HOSTPORT=BLIP")
    response = send_request(request)
    if response.status != HTTPStatus.HTTP_VERSION_NOT_SUPPORTED:
        return "Expected {}, got {}".format(str(response.status))
        return "Expected {}, got {}".format(str(HTTPStatus.HTTP_VERSION_NOT_SUPPORTED.value), str(response.status))
    return ""

#if body check if content length and content type
# check content type is correct
