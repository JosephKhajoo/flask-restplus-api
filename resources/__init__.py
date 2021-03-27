from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# from models import UserModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

api = Api(app)

db = SQLAlchemy(app)