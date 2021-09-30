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

def test_xml_file() -> str:
    errors = ""
    request = "GET /example.books.xml HTTP/1.1\r\nHost: LOL\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "text/xml", 4430)
    return errors

def test_get_empty_file() -> str:
    errors = ""
    request = "GET /emptyfile.txt HTTP/1.1\r\nHost: HOSTP\r\nConnection: close\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "text/plain", 0)
    return errors

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

def test_get_not_allowed() -> str:
    request = "GET /protected/index.html HTTP/1.1\r\nHost: HOSTP\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.METHOD_NOT_ALLOWED)

def test_get_empty_dir() -> str:
    errors = ""
    request = "GET /emptydirectory HTTP/1.1\r\nHost: HOSTP\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "text/html", 0)
    return errors

def test_get_dir_with_index() -> str:
    errors = ""
    request = "GET /foo HTTP/1.1\r\nHost: HOSTP\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "text/html", 276)
    return errors

