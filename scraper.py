import json

import requests

def create_restaurant_dict(filename: str):
    fobj = open(filename, "r")
    data = json.load(fobj)
       
    return data

def cheapest_list(data_set, search_item, length):
    
    top_list = []
    while len(top_list) <= length:
        for restaurant, menu in data_set.items():
            if restaurant in top_list:
                continue
            
            for item, price in menu.items():
                if len(top_list) == 0 or search_item in item and price <= cheapest_price:
                    cheapest_price = price
                    top_list.append((restaurant, item, price))

            break
    
    return top_list

if __name__ == "__main__":
    data = create_restaurant_dict("restaurants.json")

    print(cheapest_list(data, "cheese", 3))
    
    pass