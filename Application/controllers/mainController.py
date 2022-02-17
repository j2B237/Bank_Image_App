from Application.controllers import main
from flask import render_template


@main.route('/')
def index():
    return render_template("main/base.html", title="Flask Bank Image App")
