from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////expensesDB.db'
app.config['SECRET_KEY'] = '3847dsf@#RWEF231!@#&*&Fhrtt#@$rg*s'


db = SQLAlchemy(app)

from application import routes

