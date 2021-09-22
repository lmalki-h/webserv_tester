#!/usr/bin/env python3

import os
import sys
from typing import Callable

from tester.testsuites.parsing_request import *
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
    except Exception as e:
        print(e)
    if len(result) == 0:
        print("• {} ✅".format(colorize(test_description)))
    else:
        print("• {} ❌".format(colorize(test_description)))
        print()
        print("   {}".format(colorize(result, 91)))
    print() 

def run() -> None :

    try:
        print("{}{} ---------------------------------- Tests with malformed request -------------------------------- {}".format(C_B_MAGENTA, B_BLACK, RESET))
        """These tests can be found in tester/testsuites/parsing_request.py"""
        
        print()
        
        run_test("Test whether a request with unsupported version returns 505", test_unsupported_http_version)
        run_test("Test whether a request with a malformed header returns 400", test_malformed_header)
        run_test("Test whether a request without a host header returns 400", test_missing_host_header)
        # run_test("Test whether a malformed request timesout", test_malformed_request_timeout)
        run_test("Test whether a request with malformed start line returns 400", test_malformed_start_line)
        run_test("Test whether a request with malformed start line returns 400", test_unknown_method)
        
        print()
        print()
    
        print("{}{} ------------------------------------------- Basic tests ---------------------------------------- {}".format(C_B_MAGENTA, B_BLACK, RESET))
        """These tests can be found in tester/testsuites/basic_test.py"""
        
        print()
        
        
        
        print()
        print()
        print("{}{} ------------------------------------------- User journey --------------------------------------- {}".format(C_B_MAGENTA, B_BLACK, RESET))
        """These tests can be found in tester/testsuites/user_journey.py"""

        print()
        
        
        
        print()
        print()
        print("{}{} ------------------------------------------- Stress test ---------------------------------------- {}".format(C_B_MAGENTA, B_BLACK, RESET))

    except Exception as e:
        print(colorize(e))

if __name__ == "__main__":
    run()