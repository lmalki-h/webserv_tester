# TODO: test date is in RFC recommended format
# test http version
# test content-length matches body size
# test mime type

from http import HTTPStatus
from tester.httpserver.httpserver import * 

def test_headers(response) -> str:
    errors = ""
    #if there is a body, there must be either a content-length or a chunked encoding
    #check mime type
    #check url if redirection
    return errors

def test_status(status, expected_status) -> str:
    if status != expected_status:
        return "Expected {}, got {}\n".format(expected_status, str(status))
    return ""

def test_http_version(version) -> str:
    expected_version = 11
    if version != expected_version:
        return "Expected {}, got {}\n".format(str(expected_version), str(version))
    return ""

def test_response(response, expected_status) -> str:
    errors = ""
    errors += test_http_version(response.version)
    errors += test_status(response.status, expected_status)
    errors += test_headers(response)
    return errors


def test_payload(response, mime_type, content_length) -> str :
    errors = ""
    if response.getheader("Content-Type") == None:
        return "Expected Content-Type got none "
    if response.getheader("Content-Type") != mime_type:
        errors += "Expected {} got {}\n".format(mime_type, response.getheader("Content-Type"))
    if int(response.getheader("Content-Length")) != content_length:
        errors += "Expected {} got {} ".format(str(content_length), response.getheader("Content-Length"))
    return errors

# connection: https://datatracker.ietf.org/doc/html/rfc7230#section-6.1

def test_connection_is_closed(response) -> str:
    if response.closed != True:
        return "Connection was expected to be closed but is not"
    return ""

def test_connection_is_keep_alive(response) -> str:
    if response.closed == True:
        return "Connection was expected to be open but is closed"
    return ""