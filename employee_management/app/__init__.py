from flask import Flask  # importing flask framework

from flask_sqlalchemy import SQLAlchemy # importing sql alchemy which is used to create databases

db=SQLAlchemy()  # initializing database object


def create_app():
    # Create an instance of the Flask class by calling Flask(__name__) and adding the template folder 
    app=Flask(__name__,template_folder='../template') 

    app.config['SECRET_KEY']='secret-key'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Employee.db'
    db.init_app(app)


    return app
