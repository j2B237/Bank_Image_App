# Local party import
from Application.controllers import main


# Third party import
from flask import render_template
from datetime import datetime as dt


@main.route('/')
def index():
    year = dt.now().strftime("%Y")
    return render_template("main/base.html", title="Flask Bank Image App", categorie="Images",
                           year=year)
