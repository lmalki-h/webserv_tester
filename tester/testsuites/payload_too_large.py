from http import HTTPStatus
from tester.httpserver.httpserver import * 
from tester.testsuites.response_format import *

def test_max_body_size() -> str:
    request = "POST /upload HTTP/1.1\r\nHost: LOL\r\nContent-Length: 100000000\r\n\r\n"
    body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas maximus nisl vitae diam rutrum interdum. Maecenas imperdiet lacus velit, eget volutpat elit efficitur in. Ut ac venenatis lacus. Morbi a sollicitudin lorem. Cras et nisl ut metus ultrices congue a eget nunc. Maecenas ac purus bibendum, porta turpis nec, vestibulum neque. Fusce aliquam dolor vel mollis fermentum. In ut erat vulputate, iaculis elit non, porta dolor. Nunc ut vehicula dolor. Sed bibendum non lacus at aliquet. Vivamus pretium gravida ante sit amet luctus.Quisque sagittis, nunc vitae consectetur interdum, lectus justo consectetur odio, id vestibulum massa turpis et justo. Sed vitae odio sed massa elementum luctus at non felis. Praesent sollicitudin rhoncus metus, at fermentum tellus imperdiet a. Integer justo ante, facilisis vitae ipsum a, semper scelerisque felis. Nulla maximus interdum viverra. Proin rutrum rutrum tempor. Pellentesque molestie, ligula ut hendrerit posuere, lorem nisi euismod nibh, in turpis."
    request += body
    request += "\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.PAYLOAD_TOO_LARGE)
