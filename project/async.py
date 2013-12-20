def test(environ, start_response):
    start_response(
        "200 OK", #status
        []        #response_headers
    )
    return [b"TEST"]

def main(environ, start_response):
    start_response(
        "200 OK", #status
        []        #response_headers
    )
    return [b"MAIN"]
