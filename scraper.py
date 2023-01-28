import json

import requests

def create_restaurant_dict(filename: str):
    fobj = open(filename, "r")
    data = json.load(fobj)
       
    return data

def find_restaurants(data_set, search_item):
    restaurants = []
    
    for restaurant, menu in data_set.items():
        
        for item, price in menu.values():
            if search_item in item:
                restaurants.append({restaurant: (item, price)})
                
    return restaurants
            
def find_cheapest(data_set, search_item):
    restaurant_list = find_restaurants(data_set, search_item)
    
    for restaurant in restaurant_list:
        
        for item, price in data_set[restaurant].items():
            if search_item in item and price <= cheapest_price:
                cheapest_price = price
                cheapest_item = item
            
        return restaurant, cheapest_item, cheapest_price

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

    print(find_cheapest(data, "cheese"))
    # print(cheapest_list(data, "cheese", 3))
    
    pass