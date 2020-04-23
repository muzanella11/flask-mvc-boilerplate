from dotenv import load_dotenv
import os
from flask import Flask
from app.config.database import create_connection

load_dotenv()

def create_app(test_config = None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    # create connection
    db = create_connection()

    # get mysql instance and connection
    mysqlinstance = db.get('instance')
    mysql_connection = db.get('connection')

    app.mysql_connection = mysql_connection
    app.mysql = app.mysql_connection.cursor()

    # app.mysql.execute("show databases")

    # for i in app.mysql:
    #     print(i)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    # @app.route('/hello')
    # def hello():
    #     return 'Hello, World!'

    return app

app = create_app()

from app.controllers import *
