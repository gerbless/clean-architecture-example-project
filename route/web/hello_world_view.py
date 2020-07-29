from flask import render_template
from flask.views import MethodView


class HelloWorldView(MethodView):

    def __init__(self): pass

    def get(self):
        return render_template("hello_world.html")
