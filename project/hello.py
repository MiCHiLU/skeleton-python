#!/bin/usr/env python
# -*- coding: utf-8 -*-
import csv
import json
import pprint

from bottle import (
    default_app,
    route,
    template,
)
import httplib2

@route("/hello/<name>")
def hello(name):
    return template("hello", name=name)

@route("/weather/<location>")
def weather(location):
    base_url = "http://api.openweathermap.org/data/2.5/weather?q={0}"
    url = base_url.format(location)
    http_client = httplib2.Http(".cache")
    resp, content = http_client.request(url, "GET")
    data = json.loads(content.decode("utf-8"))
    csv_write(data)
    return template("hello", name=pprint.pformat(data))

def csv_write(data):
    with open('json.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for key, value in data.items():
            spamwriter.writerow([key, value])

app = default_app()

if __name__ == "__main__":
    from bottle import run
    run(host="localhost", port=8000, debug=True, reloader=True)
