from flask import Blueprint

main = Blueprint("main", __name__)

from Application.controllers import mainController
