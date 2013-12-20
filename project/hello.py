from bottle import route, template, default_app

@route("/hello/<name>")
def hello(name):
    return template("hello", name=name)

app = default_app()

if __name__ == "__main__":
    from bottle import run
    run(host="localhost", port=8000, debug=True, reloader=True)
