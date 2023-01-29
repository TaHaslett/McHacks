import json

import requests

def create_restaurant_dict(filename: str):
    fobj = open(filename, "r")
    data = json.load(fobj)
       
    return data

def find_restaurants(data_set, search_item):
    restaurants = {}
    
    for restaurant, menu in data_set.items():
        
        items = {}
        for item, price in menu.items():
            if search_item in item.lower():
                items[item] = price
        
        if len(items) != 0:
            restaurants[restaurant] = items
                
    return restaurants
            
def find_cheapest(data_set, search_item):
    
    restaurants = find_restaurants(data_set, search_item)
    
    overall_cheapest_restaurant = list(restaurants.keys())[0]
    overall_cheapest_item = list(list(restaurants.values())[0].keys())[0]
    overall_cheapest_price = list(list(restaurants.values())[0].values())[0]
    
    for menu in restaurants.values():
        
        cheapest_item = list(menu.keys())[0]
        cheapest_price = list(menu.values())[0]
        
        for item, price in menu.items():
            if price <= cheapest_price:
                cheapest_price = price
                cheapest_item = item 
        
        if cheapest_price <= overall_cheapest_price:
            overall_cheapest_restaurant = menu
            overall_cheapest_item = cheapest_item
            overall_cheapest_price = cheapest_price
        
    return overall_cheapest_restaurant, overall_cheapest_item, overall_cheapest_price

def cheapest_list(data_set, search_item, length):
    cheapest_list = []
    
    while len(cheapest_list) <= length:
        cheapest = find_cheapest(data_set, search_item)
        if cheapest[0] in cheapest_list:
            continue
        
        cheapest_list.append(cheapest)
    
    return cheapest_list

if __name__ == "__main__":
    data = create_restaurant_dict("restaurants.json")

    # print(find_restaurants(data, "burger"))

    print(find_cheapest(data, "cheese"))
    
    # print(cheapest_list(data, "cheese", 3))
    
    pass