import sys
from http.client import HTTPResponse
import socket
import config

def send_request(client_socket, request):
    client_socket.send(request.encode())

def connect():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((config.SERVER_ADDR, config.SERVER_PORT))
    return client_socket

def get_response(client_socket):
    response = HTTPResponse(client_socket)
    response.begin()
    return response

def connect_send_receive(request):
    client_socket = connect()
    send_request(client_socket, request)
    response = get_response(client_socket)
    return response