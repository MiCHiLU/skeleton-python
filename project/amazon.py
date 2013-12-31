#!/bin/usr/env python
# -*- coding: utf-8 -*-

import logging
import urllib2

from bottle import (
    default_app,
    route,
    template,
    get,
    post,
    request,
)

from amazonproduct import API, errors

api = API(locale='jp')

@get("/")
def amazon_get():
    return template("amazon", keywords="", results=[])

@post("/")
def amazon_post():
    keywords = request.forms.get('keywords')
    results = list()
    if keywords:
        try:
            results = api.item_search('Books', Title=keywords)
        except errors.AWSError as e:
            logging.error(u"{0}: {1}".format(e.__class__.__name__, e))
        except urllib2.URLError as e:
            logging.error("URLError: {0}".format(e))
    return template("amazon", keywords=keywords, results=results)

app = default_app()

if __name__ == "__main__":
    from bottle import run
    run(host="localhost", port=8000, debug=True, reloader=True)
