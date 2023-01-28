import json
import requests

def create_restaurant_dict(filename: str):
    fobj = open(filename, "r")
    data = fobj.load(fobj)
    
    for i in data["restaurants"]:
        print(i)
        
    return data

def cheapest_list(data_set, search_item, length):
    
    top_list = []
    while len(top_list) <= length:
        for restaurant, menu in enumerate(data_set):
            if restaurant in top_list:
                continue
            
            for item, price in enumerate(menu):
                if len(top_list) == 0 or search_item in item and price <= cheapest_price:
                    cheapest_price = price
                    top_list.append((restaurant, item, price))

            break
if __name__ == "__main__":
    create_restaurant_dict("restaurants.json")