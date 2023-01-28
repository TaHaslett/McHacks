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
        for item, price in menu.values():
            if search_item in item:
                items[item] = price
                
        restaurants[restaurant] = items
                
    return restaurants
            
def find_cheapest(data_set, search_item):
    
    restaurants = find_restaurants(data_set, search_item)
    
    overall_cheapest_restaurant = restaurants.keys()[0]
    overall_cheapest_price = restaurants[0][0]
    overall_cheapest_item = restaurants.keys()[0][0]
    
    for restaurant in restaurants:
        
        cheapest_price = restaurant[0]
        cheapest_item = restaurant.keys()[0]
        
        for item, price in restaurant.values():
            if price <= cheapest_price:
                cheapest_price = price
                cheapest_item = item
        
        if cheapest_price <= overall_cheapest_item:
            overall_cheapest_restaurant = restaurant
        
    return overall_cheapest_restaurant, cheapest_item, cheapest_price

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

    print(cheapest_list(data, "cheese", 3))
    # print(cheapest_list(data, "cheese", 3))
    
    pass