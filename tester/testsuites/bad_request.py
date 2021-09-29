from http import HTTPStatus
from tester.httpserver.httpserver import * 
from tester.testsuites.response_format import *


# request line: https://datatracker.ietf.org/doc/html/rfc7230#section-3.1.1

def test_malformed_request() -> str:
    request = "qwerty\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_malformed_request_timeout() -> str:
    request = "qwerty"
    # response = connect_send_receive(request)
    #TODO: connect send, attend x seconds et verifie que la connexion est closed
    return "" #test_response(response, HTTPStatus.BAD_REQUEST)

def test_unknown_method() -> str:
    request = "BLIBLOP / HTTP/1.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_malformed_start_line() -> str:
    request = "get / HTTP/1.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_malformed_start_line2() -> str:
    request = "GET  /  HTTP/1.1\r\nHost: LOL\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

# headers: https://datatracker.ietf.org/doc/html/rfc7230#section-3.2

def test_malformed_header() -> str:
    request = "GET /foo HTTP/1.1\r\nHost: tester\r\nHeader with missing colon\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_either_content_length_or_chunked() -> str:
    request = "GET / HTTP/0.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\nthis is a body isnt it\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_missing_header_name() -> str:
    request = "GET / HTTP/1.1\r\nHost: LOL\r\n: empty\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_malformed_header() -> str:
    request = "GET / HTTP/1.1\r\nHost : LOL\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_missing_header_body() -> str:
    request = "POST /upload/test HTTP/1.1\r\nHost : LOL\r\n\r\n"
    request += "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in mauris id ipsum vestibulum morbi.\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST) #quel code de retour ??

def test_negative_content_length() -> str:
    request = "POST /upload/test2\r\nHost: LOL\r\nContent-Length: -1\r\n\r\n"
    body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer faucibus venenatis mauris eleifend.\r\n"
    request += body
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_alpha_content_length() -> str:
    request = "POST /upload/test2\r\nHost: LOL\r\nContent-Length: NODIGIT\r\n\r\n"
    body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer faucibus venenatis mauris eleifend.\r\n"
    request += body
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_duplicate_content_length() -> str:
    request = "POST /upload/test2\r\nHost: LOL\r\nContent-Length: 100\r\nContent-Length: 100\r\n\r\n"
    body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer faucibus venenatis mauris eleifend.\r\n"
    request += body
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

# host : https://datatracker.ietf.org/doc/html/rfc7230#section-5.4

def test_missing_host_header() -> str:
    request = "GET /foo HTTP/1.1\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_duplicate_host_header() -> str:
    request = "GET / HTTP/1.1\r\nHost: LOL\r\nHost: LOL\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)

def test_multiple_host_header() -> str:
    request = "GET / HTTP/1.1\r\nHost: LOL\r\nHost: BOO\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.BAD_REQUEST)