import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Initialize Flask app
app = Flask(__name__)

# Set the database URI to SQLite (or PostgreSQL if needed)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///expensesDB.db')  # Use SQLite or PostgreSQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for performance
app.config['SECRET_KEY'] = '3847dsf@#RWEF231!@#&*&Fhrtt#@$rg*s'  # Secret key for sessions

# Initialize SQLAlchemy (only once)
db = SQLAlchemy(app)

# Import routes after app and db setup
from application import routes
