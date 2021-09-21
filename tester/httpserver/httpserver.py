import sys
from http.client import HTTPResponse
import socket
import config

def send_request(request: str):
    #connect to server and send request
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((config.SERVER_ADDR, config.SERVER_PORT))
    client.send(request.encode())
    
    #get response
    response = HTTPResponse(client)
    response.begin()
    return response

def replace_placeholder(s: str, macro: str):
    values = macro.split('=')
    # print("key = {} value = {}", values[0], values[1])
    s.replace(values[0], values[1])
    return s

def make_request(request_file: str, macro: str):
    full_path = "tester/requests/" + request_file
    file = open(full_path, 'r')
    request = replace_placeholder(file.read(), macro)

    #turn the file into a request, changed <HOSTPORT> par la var
    return request