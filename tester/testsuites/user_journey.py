import socket
import config
import sys
from http.client import HTTPResponse
from http import HTTPStatus
from tester.testsuites.response_format import *
from tester.httpserver.httpserver import *


def user_journey():
    """ Connects to the server and performs a few requests using the same socket """"
    errors = ""
    # connect to server
    client_socket = connect()
    
    # get a html page
    request1 = "GET simpleindex.html HTTP/1.1\r\nHost: Tester\r\nConnection: keep-alive\r\n\r\n"
    send_request(client_socket, request1)
    response1 = get_response(client_socket)
    errors += test_response(response1, HTTPStatus.OK)
    errors += test_payload(response1, "text/html", 286)
    
    # get an image
    request2 = "GET image1.jpg HTTP/1.1\r\nHost: Tester\r\n\r\n"
    send_request(client_socket, request2)
    response2 = get_response(client_socket)
    errors += test_response(response1, HTTPStatus.OK)
    errors += test_payload(response, "image/jpg", )

    # upload a file

    # get the uploaded file
    request2 = "GET /upload/myuploadedfile.html HTTP/1.1\r\nHost: Tester\r\n\r\n"
    send_request(client_socket, request2)
    response2 = get_response(client_socket)
    errors += test_response(response1, HTTPStatus.OK)
    errors += test_payload(response, "text/html", )


    # get unknown directory

    # delete from protected directory without credentials

    # delete uploaded file

    # delete protected file with incorrect credentials

    # delete protected file with correct credentials
