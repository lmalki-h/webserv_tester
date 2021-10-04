#!/usr/bin/env python3

import os
import sys
from typing import Callable

from tester.testsuites.bad_request import *
from tester.testsuites.delete_request import *
from tester.testsuites.get_request import *
from tester.testsuites.internal_server_error import *
from tester.testsuites.payload_too_large import *
from tester.testsuites.unsupported_version import *
from tester.testsuites.uri_too_long import *

import config

#colors
RESET = "\033[0m"
C_BLACK = "\033[30m"
C_RED = "\033[31m"
C_GREEN = "\033[32m"
C_YELLOW = "\033[33m"
C_BLUE = "\033[34m"
C_MAGENTA = "\033[35m"
C_CYAN = "\033[36m"
C_WHITE = "\033[37m"
C_GRAY = "\033[90m"

#bold & colors
C_B_BLACK = "\033[30;01m"
C_B_RED = "\033[31;01m"
C_B_GREEN = "\033[32;01m"
C_B_YELLOW = "\033[33;01m"
C_B_BLUE = "\033[34;01m"
C_B_MAGENTA = "\033[35;01m"
C_B_GRAY = "\033[36;01m"
C_B_WHITE = "\033[37;01m"
C_B_GRAY = "\033[90;01m"

# color background
B_BLACK = "\033[40m"
B_RED = "\033[41m"
B_GREEN = "\033[42m"
B_YELLOW = "\033[43m"
B_BLUE = "\033[44m"
B_MAGENTA = "\033[45m"
B_GRAY = "\033[46m"
B_WHITE = "\033[47m"

def colorize(s: str, code=37) -> str :
    """colorize the string, default to blue"""
    return f"\033[{code}m{s}\033[0m"

def run_test(test_description: str, test: Callable):
    try:
        result = test()
        if len(result) == 0:
            print(f"{colorize(test_description):<100}{'✅':>2}")
            # print("• {} ✅".format(colorize(test_description)))
        else:
            print(f"{colorize(test_description):<100}{'❌':>2}")
            # print("• {} ❌".format(colorize(test_description)))
            print()
            print("   {}".format(colorize(result, 91)))
    except Exception as e:
        print(e)
    print() 

def run_malformed_request() -> None:
    try:
        print("{}{} ------------------------------------------- Tests with malformed request ----------------------------------- {}".format(C_B_BLUE, B_BLACK, RESET))
        """These tests can be found in tester/testsuites/parsing_request.py"""
        
        print()
        # run_test("Test whether a request with duplicate headers returns 200")
        # run_test("Test whether a header too long returns a 4XX", test_header_too_long)
        # run_test("Test whether a request with malformed start line returns 400", test_unknown_method)
        # run_test("Test whether a malformed request timesout", test_malformed_request_timeout)
        # run_test("Test whether a request with an invalid host header returns a 400", test_invalid_host)

        run_test("Test whether a request with unsupported version returns 505", test_unsupported_http_version)
        run_test("Test whether a request with a header missing colon returns 400", test_malformed_header2)
        run_test("Test whether a request with header with extra space returns 400", test_malformed_header)
        run_test("Test whether a request without a host returns 400", test_missing_host_header)
        run_test("Test wehther a request with duplicate host returns 400", test_duplicate_host_header)
        run_test("Test wehther a request with two host headers returns 400", test_multiple_host_header)
        run_test("Test whether a request with header missing name returns 400", test_missing_header_name)
        run_test("Test whether a request with malformed method returns 400", test_malformed_start_line)
        run_test("Test whether a request with malformed start line returns 400", test_malformed_start_line2)
        # run_test("Test whether a request with body size superior to max returns 400", test_max_body_size)
        run_test("Test whether a request with body and missing header returns 400", test_missing_header_body)
        run_test("Test whether returns a file with multiple dot returns properly", test_xml_file)
        run_test("Test whether a missing error page returns 500", test_error_and_missing_error_page)
        run_test("Test whether a request with uri superior to max returns 414", test_max_uri_length)
        run_test("Test whether a request with negative content-length returns 400", test_negative_content_length)
        run_test("Test whether a request with content-length header containing alpha characters returns 400", test_alpha_content_length)
        run_test("Test whether a request with duplicate content-length header returns 400", test_duplicate_content_length)
        # run_test("Test whether a request with valid content-length but no body returns ")
        print()
        print()
    except Exception as e:
        print(colorize(e))

def run_get_tests() -> None:
    try:
        print("{}{} ------------------------------------------- Tests for GET request ------------------------------------------ {}".format(C_B_BLUE, B_BLACK, RESET))    
        """These tests can be found in tester/testsuites/basic_test.py"""
        
        print()
        run_test("Simple test with html page", test_get_url_ok)
        run_test("Test whether a request returns a gif properly", test_gif_file)
        run_test("Test whether a request returns a jpg properly", test_jpeg_file)
        run_test("Test whether a request returns a jpeg properly", test_jpg_file)
        run_test("Test whether a request returns a png properly", test_png_file)
        run_test("Test whether a request returns an empty file with content-length = 0", test_get_empty_file)
        run_test("Test whether returns a 405 on protected dir", test_get_not_allowed)
        run_test("Test whether a request on empty dir returns 200 with content-length = 0", test_get_empty_dir)
        run_test("Test whether a request on dir with index returns index", test_get_dir_with_index)
        # run_test("Test whether a request returns a xml properly", test_xml_file)
        # tester la requete get
            # tester un get dir sur autoindex           
        print()
        print()
    except Exception as e:
        print(colorize(e))
    
def run_post_tests() -> None:
    try:
        print("{}{} ------------------------------------------- Tests for POST request ----------------------------------------- {}".format(C_B_BLUE, B_BLACK, RESET))
        print()
        
        # tester la requete post
            # tester un post avec une query encode
            # tester un post avec une query non encode
            # tester un post sur une target non existante
            # tester un post correcte
            # tester un post correcte avec un fichier de 10M bytes

        print()
        print()
    except Exception as e:
        print(colorize(e))

def run_delete_tests() -> None:
    try:
        print("{}{} ------------------------------------------- Tests for DELETE request --------------------------------------- {}".format(C_B_BLUE, B_BLACK, RESET))
        # tester la requete delete
        run_test("Test whether properly delete a file", test_delete_ok)
        run_test("Test whether returns a 405 on protected dir", test_delete_not_allowed)          #returns 500 instead of 405
        # run_test("Test whether returns a 404 on a missing file", test_delete_missing)             #runs forever
        run_test("Test whether returns a 404 on a file already deleted", test_already_deleted)    #returns 500 instead of 404
        run_test("Test whether properly delete a directory", test_delete_dir)                     #returns 500 instead of 200

        print()
        print()
    except Exception as e:
        print(colorize(e))

def run_cgi_tests() -> None:
    try:
        print("{}{} ------------------------------------------- Tests CGI  ----------------------------------------------------- {}".format(C_B_BLUE, B_BLACK, RESET))
        # tester le cgi
            # tester surle cgi headers

    except Exception as e:
        print(colorize(e))

def run_chunk_tests() -> None:
    try:
        print("{}{} ------------------------------------------- Tests for chunk ------------------------------------------------ {}".format(C_B_BLUE, B_BLACK, RESET))
        # tester le chunk
        # run_test("Test whether a request with content-length and transfer encoding chunk headers return ")

        print()
        print()
    except Exception as e:
        print(colorize(e))

def run() -> None :
    run_malformed_request()
    run_get_tests()
    run_delete_tests()
    run_post_tests()
    run_cgi_tests()
    run_chunk_tests()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        run()
    elif str(sys.argv[1]) == "syntax":
        run_malformed_request()
    elif str(sys.argv[1]) == "get":
        run_get_tests()
    elif str(sys.argv[1]) == "delete":
        run_delete_tests()
    elif str(sys.argv[1]) == "post":
        run_post_tests()
    elif str(sys.argv[1]) == "cgi":
        run_cgi_tests()
    elif str(sys.argv[1]) == "chunked":
        run_chunk_tests()
