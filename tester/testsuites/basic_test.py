# TODO: test that the connection actually closes when connection close header
# TODO: test that connection keeps alive when connection keep alive header

# TODO: test content-length

# TODO: test whether missing resource return 404

from http import HTTPStatus
from tester.httpserver.httpserver import * 

def test_get_url_ok() -> str:
    request = "GET / HTTP/0.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    # request = make_request("unsupported_http_version.http", "HOSTPORT=BLIP")
    response = send_request(request)
    if response.status != HTTPStatus.OK:
        return "Expected {}, got {}".format(str(HTTPStatus.OK.value), str(response.status))
    return ""

# def test_method_not_implemented() -> str:

# def test_method_not_allowed() -> str:

# Test whether a JPEG image returns 200 with proper Content-Length on GET

# test_get_empty_text_file: Test whether an empty file returns zero bytes with 200 on GET