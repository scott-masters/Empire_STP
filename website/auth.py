# This page has received basic logging.

import flask as fl

auth = fl.Blueprint("auth", __name__)

@auth.route('/', methods = ["GET"])
def home():
    """
    This is the home page.
    """
    return fl.render_template("home.html")