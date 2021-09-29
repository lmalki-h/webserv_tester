def test_xml_file() -> str:
    errors = ""
    request = "GET /example.books.xml HTTP/1.1\r\nHost: LOL\r\n\r\n"
    response = connect_send_receive(request)
    errors += test_response(response, HTTPStatus.OK)
    errors += test_payload(response, "text/xml", 4430)
    return errors
