from http import HTTPStatus
from tester.httpserver.httpserver import * 
from tester.testsuites.response_format import *

def test_get_url_ok() -> str:
    request = "GET simpleindex.html HTTP/1.1\r\nHost: Tester\r\n\r\n"
    response = send_request(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "text/html", 286)
    return errors

# def test_method_not_implemented() -> str:

# def test_method_not_allowed() -> str:

# Test whether a JPEG image returns 200 with proper Content-Length on GET

# test_get_empty_text_file: Test whether an empty file returns zero bytes with 200 on GET

def test_get_empty_file() -> str:
    errors = ""
    request = "GET /emptyfile.txt HTTP/1.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = send_request(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "text/plain", 0)
    return errors

# def test_encoded_query() -> str:

# def test_invalid_file_extension -> str :
# simpleindex.hmtl

# def test_gif_file -> str :