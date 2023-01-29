from flask import Flask
from scraper import *

app = Flask(__name__)

data = create_restaurant_dict("restaurants.json")
    
the_list = create_list(data, "burger", 3, True)

@app.route("/")
def main():
    return "Welcome to my Flask page!" + str(the_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)