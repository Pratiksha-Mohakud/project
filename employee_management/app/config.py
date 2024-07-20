# setting up configurations

# Imports the os module to access environment variables and other OS-related functionalities.
import os  
basedir=os.path.abspath(os.path.dirname(__file__))
class config:
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'app,db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False