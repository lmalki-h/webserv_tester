from http import HTTPStatus
from tester.httpserver.httpserver import * 
from tester.testsuites.response_format import *

def test_delete_not_allowed() -> str:
    errors = ""
    request = "DELETE /get-only HTTP/1.1\r\nHost: LOL\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.METHOD_NOT_ALLOWED)
    return errors

def test_delete_ok() -> str:
    request = "DELETE /removeme/removeme.txt HTTP/1.1\r\nHost: LOL\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.OK)

def test_delete_missing() -> str:
    request = "DELETE /emptydir/missingfile.txt HTTP/1.1\r\nHost: LOL\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.NOT_FOUND)

def test_already_deleted() -> str:
    request = "DELETE /removeme/removeme.txt HTTP/1.1\r\nHost: LOL\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.NOT_FOUND)

def test_delete_dir() -> str:
    request = "DELETE /removeme HTTP/1.1\r\nHost: LOL\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.OK)