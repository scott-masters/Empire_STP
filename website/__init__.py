# A file with the specific __init__.py name turns our website into a python package.

import flask as fl
import flask_sqlalchemy as fs
import datetime as dt
import os
import logging
import time

from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers = 5)

db = fs.SQLAlchemy()
db_name = "database.db"

logging.basicConfig(
    filename = "database.log",
    format = '%(asctime)s: %(name)s - %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__) # __name__
logging.getLogger('werkzeug').setLevel(logging.CRITICAL + 1)
# logging.getLogger('werkzeug').setLevel(logging.DEBUG)
logging.getLogger('website').setLevel(logging.DEBUG)

logger.info("Initial message to test our logger")

def create_app():
    """
    This function initialises our app to run a website, it was mostly copied
    from this tutorial: https://www.youtube.com/watch?v=dam0GPOAvVI&t=4228s
    """
    app = fl.Flask(__name__)
    app.config["SECRET_KEY"] = "keyyy"

    # This tells flask the location where the database is stored 
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_name}"
    db.init_app(app)

    from website.views import views
    from website.auth import auth

    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(auth, url_prefix = "/")

    return app
