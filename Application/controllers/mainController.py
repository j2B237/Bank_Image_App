# Local party import
from Application.controllers import main


# Third party import
from flask import render_template
from datetime import datetime as dt


@main.route('/')
def index():
    """ Function to render the home page view """
    year = dt.now().strftime("%Y")
    return render_template("main/index.html", title="Flask Bank Image App", categorie="Images",
                           year=year)


@main.route("/image-view")
def image_page():
    """ Function to render image view """
    return render_template("main/image_page.html", title="Image page", categorie="Images")


@main.route("/video-view")
def video_page():
    """ Function to render video view """
    return render_template("main/video_page.html", title="Video page", categorie="Vidéos")