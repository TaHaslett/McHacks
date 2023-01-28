import json
import requests

def create_restaurant_dict(filename: str):
    fobj = open(filename, "r")
    data = fobj.load(fobj)
    
    for i in data["restaurants"]:
        print(i)
        
if __name__ == "__main__":
    create_restaurant_dict("restaurants.json")
    