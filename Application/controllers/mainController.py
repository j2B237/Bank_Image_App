# Local party import
from Application.controllers import main

# Third party import
from flask import render_template
from datetime import datetime as dt


@main.route('/')
def index():
    """ Function to render the home page view """
    img_accueil = "video-detail-1.jpg"
    year = dt.now().strftime("%Y")
    return render_template("main/index.html", title="Africa Art & Artists", categorie="Images",
                           year=year, img=img_accueil)


@main.route("/image-view")
def image_page():
    """ Function to render image view """
    year = dt.now().strftime("%Y")
    img_accueil = "seth-doyle-zf9_yiAekJs-unsplash.jpg"
    return render_template("main/image_page.html", title="Image page", categorie="Photos", year=year, img=img_accueil)


@main.route('/illustration-view')
def illustration_page():
    """ Function to render illustration view """
    year = dt.now().strftime("%Y")
    img_accueil = "seth-doyle-zf9_yiAekJs-unsplash.jpg"
    return render_template("main/video_page.html", title="Video page", categorie="Vidéos", year=year, img=img_accueil)


@main.route("/video-view")
def video_page():
    """ Function to render video view """
    year = dt.now().strftime("%Y")
    img_accueil = "paul-zoetemeijer-ekBOf6sJYYo-unsplash.jpg"
    return render_template("main/video_page.html", title="Video page", categorie="Vidéos", year=year, img=img_accueil)


@main.route('/music-view')
def music_page():
    """ Function to render music view """
    year = dt.now().strftime("%Y")
    img_accueil = "seth-doyle-zf9_yiAekJs-unsplash.jpg"
    return render_template("main/video_page.html", title="Video page", categorie="Vidéos", year=year, img=img_accueil)


@main.route("/image/<image_title>")
def view_image(image_title):
    """" Function to render an image view """
    year = dt.now().strftime("%Y")
    return render_template("catalogue/view_image.html", title="Afro A&A : {}".format(image_title.replace('-', ' '),
                                                                                     year=year))
