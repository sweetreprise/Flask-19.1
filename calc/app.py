# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def calc_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = add(a, b)

    return f"{answer}"

@app.route('/sub')
def calc_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = sub(a, b)

    return f"{answer}"

@app.route('/mult')
def calc_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = mult(a, b)

    return f"{answer}"

@app.route('/div')
def calc_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = div(a, b)

    return f"{answer}"

functions = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<func>')
def calc_all(func):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = functions[func](a, b)

    return f"{answer}"
