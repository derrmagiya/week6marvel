from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_envvar('.env')

db = SQLAlchemy(app)