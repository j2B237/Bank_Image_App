from flask import Flask

app = Flask(__name__)

# Blueprint registration
from Application.controllers import main as main_blueprint

app.register_blueprint(main_blueprint)
