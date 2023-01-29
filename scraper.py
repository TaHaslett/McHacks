import json

# hello

def create_restaurant_dict(filename: str):
    fobj = open(filename, "r")
    data = json.load(fobj)
    fobj.close()
    
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
            
    if len(restaurant) == 0:
        raise ValueError
                
    return restaurants
            
def find_cheapest(data_set, search_item):
    
    restaurants = find_restaurants(data_set, search_item)
    
    overall_cheapest_restaurant = list(restaurants.keys())[0]
    overall_cheapest_item = list(list(restaurants.values())[0].keys())[0]
    overall_cheapest_price = list(list(restaurants.values())[0].values())[0]
    
    for restaurant, menu in restaurants.items():
        
        cheapest_item = list(menu.keys())[0]
        cheapest_price = list(menu.values())[0]
        
        for item, price in menu.items():
            if price < cheapest_price:
                cheapest_price = price
                cheapest_item = item 
        
        if cheapest_price < overall_cheapest_price:
            overall_cheapest_restaurant = restaurant
            overall_cheapest_item = cheapest_item
            overall_cheapest_price = cheapest_price
        
    return overall_cheapest_restaurant, overall_cheapest_item, overall_cheapest_price

def remove_menu_item(data_set, restaurant, menu_item):
    del data_set[restaurant][menu_item]

def cheapest_list(data_set, search_item, length):
    cheapest_list = []
    
    for i in range(length):
        try:
            cheapest = find_cheapest(data_set, search_item)
            cheapest_list.append(cheapest)
            remove_menu_item(data_set, cheapest[0], cheapest[1])
        except ValueError:
            break
        
    return cheapest_list

if __name__ == "__main__":
    data = create_restaurant_dict("restaurants.json")
    
    print(cheapest_list(data, "fatcarons", 3))
    
    pass