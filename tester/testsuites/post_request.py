

def test_post_empty_dir() -> str:
    request = "POST /emptydirectory HTTP/1.1\r\nHost: HOSTP\r\n\r\n"
    response = connect_send_receive(request)
    return test_response(response, HTTPStatus.OK)


def test_post_ok() -> str:
    request = "POST /upload/example.txt HTTP/1.1\r\nHost: HOSTP\r\n\r\n"