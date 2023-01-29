from flask import Flask, render_template, request
import scraper as s

DATABASE_FILE_NAME = "fake_restaurants.json"

app = Flask(__name__)
    
    
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
        
        boogeeness = "bougie_mode" in form_data
             
        data = s.create_restaurant_dict(DATABASE_FILE_NAME)
        post = s.create_post(data, form_data["item"], 3, boogeeness)
        
        return render_template("results.html", post=post, search=form_data["item"], length=len(post))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)