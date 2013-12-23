#!/bin/usr/env python
# -*- coding: utf-8 -*-

from bottle import (
    default_app,
    route,
    template,
)

@route("/")
def amazon():
    return template("amazon")

app = default_app()

if __name__ == "__main__":
    from bottle import run
    run(host="localhost", port=8000, debug=True, reloader=True)
