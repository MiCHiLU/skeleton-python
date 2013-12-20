#!/usr/bin/env sh
#gunicorn -k "aiohttp.worker.AsyncGunicornWorker" async:main;
gunicorn -k "aiohttp.worker.AsyncGunicornWorker" async:test;
