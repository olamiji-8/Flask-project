from flask import Flask , render_template , url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///'
@app.route("/")
def hello_world():
    return render_template("index.html")