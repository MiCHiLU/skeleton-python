#!/bin/usr/env python
# -*- coding: utf-8 -*-

from bottle import (
    default_app,
    route,
    template,
    get,
    post,
    request,
)

@get("/")
def amazon_get():
    return template("amazon")

@post("/")
def amazon_post():
    keywords = request.forms.get('keywords')
    return template("amazon", keywords=keywords)

app = default_app()

if __name__ == "__main__":
    from bottle import run
    run(host="localhost", port=8000, debug=True, reloader=True)
