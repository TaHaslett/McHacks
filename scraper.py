import json

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
            if search_item.lower() in item.lower():
                items[item] = price
        
        if len(items) != 0:
            restaurants[restaurant] = items
            
    if len(restaurants) == 0:
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

def find_expensive(data_set, search_item):
    
    restaurants = find_restaurants(data_set, search_item)
    
    overall_expensive_restaurant = list(restaurants.keys())[0]
    overall_expensive_item = list(list(restaurants.values())[0].keys())[0]
    overall_expensive_price = list(list(restaurants.values())[0].values())[0]
    
    for restaurant, menu in restaurants.items():
        
        expensive_item = list(menu.keys())[0]
        expensive_price = list(menu.values())[0]
        
        for item, price in menu.items():
            if price > expensive_price:
                expensive_price = price
                expensive_item = item 
        
        if expensive_price > overall_expensive_price:
            overall_expensive_restaurant = restaurant
            overall_expensive_item = expensive_item
            overall_expensive_price = expensive_price
        
    return overall_expensive_restaurant, overall_expensive_item, overall_expensive_price

def remove_menu_item(data_set, restaurant, menu_item):
    del data_set[restaurant][menu_item]

def create_list(data_set: dict, search_item: str, length: int, bougie: bool):
    best_list = []
    
    for i in range(length):
        try:
            if bougie:
                best = find_expensive(data_set, search_item)
            else:
                best = find_cheapest(data_set, search_item)
            
            best_list.append(best)
            remove_menu_item(data_set, best[0], best[1])
        except ValueError:
            break
        
    return best_list

def create_post(data_set, search_item, length, bougie):
    tup_list = create_list(data_set, search_item, length, bougie)
    final_list = []
    for tup in tup_list:
        print(tup)
        print(tup[0])
        dict_e = {}
        dict_e['Restaurant'] = tup[0]
        dict_e['Item'] = tup[1]
        dict_e['Price'] = str(tup[2])
        final_list.append(dict_e)  
    return final_list
    

if __name__ == "__main__":
    data = create_restaurant_dict("restaurants.json")
    
    print(create_list(data, "burger", 4, False))
    print(create_post(data, "burger", 4, False))