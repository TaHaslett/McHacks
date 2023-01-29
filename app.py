from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from scraper import *

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def main():
    title = "My page"
    name= "Tristan"
    
    return render_template("index.html", title=title, name=name)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)