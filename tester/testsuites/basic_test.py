from http import HTTPStatus
from tester.httpserver.httpserver import * 
from tester.testsuites.response_format import *

def test_get_url_ok() -> str:
    errors = ""
    request = "GET /simplestindex.html HTTP/1.1\r\nHost: Tester\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "text/html", 286)
    return errors

# def test_method_not_implemented() -> str:

def test_method_not_allowed() -> str:
    errors = ""
    request = "DELETE /get-only HTTP/1.1\r\nHost: LOL\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.METHOD_NOT_ALLOWED)
    return errors

# Test whether a JPEG image returns 200 with proper Content-Length on GET

# test_get_empty_text_file: Test whether an empty file returns zero bytes with 200 on GET

def test_get_empty_file() -> str:
    errors = ""
    request = "GET /emptyfile.txt HTTP/1.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "text/plain", 0)
    return errors

# def test_invalid_file_extension -> str :
#     request = "GET /simpleindex.hmtl HTTP/1.1\r\nHost: RE\r\nConnection: close\r\n\r\n"
#     response += connect_send_receive(request)
#     errors += test_response(response, HTTPStatus.)

def test_gif_file() -> str:
    errors = ""
    request = "GET /images/sandler.gif HTTP/1.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "image/gif", 1864794)
    return errors

def test_jpg_file() -> str:
    errors = ""
    request = "GET /images/image1.jpg HTTP/1.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "image/jpeg", 1737005)
    return errors

def test_jpeg_file() -> str:
    errors = ""
    request = "GET /images/image2.jpeg HTTP/1.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "image/jpeg", 1497208)
    return errors

def test_png_file() -> str:
    errors = ""
    request = "GET /images/car.png HTTP/1.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "image/png", 205139)
    return errors
