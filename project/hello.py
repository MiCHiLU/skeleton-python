from bottle import route, template, default_app
import httplib2
import json
import pprint
import logging

@route("/hello/<name>")
def hello(name):
    return template("hello", name=name)

@route("/weather/<location>")
def weather(location):
    #location = "London,uk"
    url = "http://api.openweathermap.org/data/2.5/weather?q={0}"
    url = url.format(location)
    h = httplib2.Http(".cache")
    #resp, content = h.request(url, "GET")
    response = h.request(url, "GET")
    resp = response[0]
    content = response[1]
    #logging.error(resp)
    #logging.error(content)
    data = json.loads(content.decode("utf-8"))
    write(data)
    return template("hello", name=pprint.pformat(data))

import csv
def write(data):
    with open('json.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for key, value in data.items():
            spamwriter.writerow([key, value])

app = default_app()

if __name__ == "__main__":
    from bottle import run
    run(host="localhost", port=8000, debug=True, reloader=True)
