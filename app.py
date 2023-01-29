from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
import scraper as s

app = Flask(__name__)

data = s.create_restaurant_dict("restaurants.json")

class FindFoodForm(FlaskForm):
    food_item = StringField("search", validators=[DataRequired(), Length(max=20)])
    
    
@app.route("/")
@app.route("/home")
def main():
    
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/results", methods=["POST", "GET"])
def results():
    if request.method == "GET":
        return f""
    
    if request.method == "POST":
        form_data = request.form
        food = form_data["item"]
        
        
        
        return render_template("results.html", form_data=form_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)