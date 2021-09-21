import config
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

def test_malformed_header() -> str:
    request = "GET /foo HTTP/1.1\r\nHost: tester\r\nHeader with missing colon\r\n\r\n"
    response = send_request(request)
    if response.status != HTTPStatus.BAD_REQUEST:
        return "Expected {}, got {}".format(str(HTTPStatus.BAD_REQUEST.value), str(response.status))
    return ""

def test_missing_host_header() -> str:
    request = "GET /foo HTTP/1.1\r\n\r\n"
    response = send_request(request)
    if response.status != HTTPStatus.BAD_REQUEST:
        return "Expected {}, got {}".format(str(HTTPStatus.BAD_REQUEST.value), str(response.status))
    return ""

def test_malformed_request() -> str:
    request = "qwerty\r\n"
    response = send_request(request)
    if response.status != HTTPStatus.BAD_REQUEST:
        return "Expected {}, got {}".format(str(HTTPStatus.BAD_REQUEST.value), str(response.status))
    return ""

def test_malformed_request_timeout() -> str:
    request = "qwerty"
    response = send_request(request)
    if response.status != HTTPStatus.BAD_REQUEST:
        return "Expected {}, got {}".format(str(HTTPStatus.BAD_REQUEST.value), str(response.status))
    return ""

def test_either_content_length_or_chunked() -> str:
    request = "GET / HTTP/0.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\nthis is a body isnt it\r\n\r\n"
    response = send_request(request)
    if response.status != HTTPStatus.BAD_REQUEST:
        return "Expected {}, got {}".format(str(HTTPStatus.BAD_REQUEST.value), str(response.status))
    return ""

# def test_file_size_too_large() -> str:
    #TODO: file size > to server client max body size

def test_unknown_method() -> str:
    request = "BLIBLOP / HTTP/0.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = send_request(request)
    if response.status != HTTPStatus.BAD_REQUEST:
        return "Expected {}, got {}".format(str(HTTPStatus.BAD_REQUEST.value), str(response.status))
    return ""

def test_malformed_start_line() -> str:
    request = "get / HTTP/0.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = send_request(request)
    if response.status != HTTPStatus.BAD_REQUEST:
        return "Expected {}, got {}".format(str(HTTPStatus.BAD_REQUEST.value), str(response.status))
    return ""
