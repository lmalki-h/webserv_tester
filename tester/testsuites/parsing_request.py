from http import HTTPStatus
from tester.httpserver.httpserver import * 
from tester.testsuites.response_format import *

def test_unsupported_http_version() -> str:
    request = "GET / HTTP/0.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.HTTP_VERSION_NOT_SUPPORTED)

def test_malformed_header() -> str:
    request = "GET /foo HTTP/1.1\r\nHost: tester\r\nHeader with missing colon\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_missing_host_header() -> str:
    request = "GET /foo HTTP/1.1\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_malformed_request() -> str:
    request = "qwerty\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_malformed_request_timeout() -> str:
    request = "qwerty"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_either_content_length_or_chunked() -> str:
    request = "GET / HTTP/0.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\nthis is a body isnt it\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

# def test_file_size_too_large() -> str:
    #TODO: file size > to server client max body size

def test_unknown_method() -> str:
    request = "BLIBLOP / HTTP/1.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_malformed_start_line() -> str:
    request = "get / HTTP/1.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)


# TODO: Test duplicate stuff