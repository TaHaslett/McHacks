from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from scraper import *

app = Flask(__name__)

class BasicForm(FlaskForm):
    ids = StringField("ID",validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/", methods =['POST','GET'])
def main():
    form = BasicForm()
    return render_template("index.html",form = form)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)