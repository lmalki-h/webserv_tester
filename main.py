#!/usr/bin/env python3

import os
import sys
from tester.testsuites.parsing_request import *
import config
from typing import Callable

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

def colorize(str, code=34) -> str :
    return f"\033[{code}m{str}\033[0m"

def run_test(test_description: str, test: Callable):
    print(colorize(test_description))
    try:
        result = test()
    except Exception as e:
        print(e)
    if len(result) == 0:
        print("{} PASSED! {}".format(C_GREEN, RESET))
    else:
        print(colorize(result, 91))

def run() -> None :

    print("Starting the tests....")
    print()
    print()
    try:
        run_test("Test whether a request with unsupported version returns 505", test_unsupported_http_version)
        run_test("Test whether a request with a malformed header returns 400", test_malformed_header)
        run_test("Test whether a request without a host header returns 400", test_missing_host_header)
        # run_test("Test whether a malformed request timesout", test_malformed_request_timeout)
        run_test("Test whether a request with malformed start line returns 400", test_malformed_start_line)
    except Exception as e:
        print(colorize(e))

if __name__ == "__main__":
    run()




    # def print_help():
    #     print("")
    #     print("Usage:")
    #     print("./main.py [<host>]:[<port>] [<suite-id> [<test-id>]]")
    #     print("")
    #     print("<host>       Hostname or IP address of the server to be tested, default to 'localhost'")
    #     print("<port>       Port number of the server to be tested, default to '8080'")
    #     print("<suite-id>   ID of a test suite, default to all test suites")
    #     print("<test-id>    ID of an individual test function")
    #     print("")
    
    # if {"-h", "--help"}.intersection(sys.argv):
    #     print_help()
    #     sys.exit(0)
    
    # if len(sys.argv) < 2:
    #     print("")
    #     print("Here is a list of the available tests")
    #     for sname, suite in testsuites.items():
    #         print()
    #         print(f"{f' Test Suite: {colorize(sname)} ':=^80}")
    #         for fname, func in suite().testcases.items():
    #             print(f"* {colorize(fname)}: {colorize(func.__doc__, 96)}")
    #     print()
    #     sys.exit(0)