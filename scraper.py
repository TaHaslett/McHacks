import json
import requests

def create_restaurant_dict(filename: str):
    fobj = open(filename, "r")
    data = fobj.load(fobj)
    
    for i in data["restaurants"]:
        print(i)
        
    return data

def cheapest_list(data_set, food_item, length):
    
    top = []
    while length(top) <= length:
        for restaurant, menu in enumerate(data_set):
            if restaurant in top:
                continue
            
            for item in restaurant:
                pass
        
if __name__ == "__main__":
    create_restaurant_dict("restaurants.json")