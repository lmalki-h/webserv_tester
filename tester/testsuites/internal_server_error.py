def test_error_and_missing_error_page() -> str:
    errors = ""
    request = "GET /error/nopage HTTP/1.1\r\nHost: LOL\r\n\r\n" #missing page + error configuration missing error_pages still returns an error
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.INTERNAL_SERVER_ERROR)
    return errors
