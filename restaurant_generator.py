import cohere
import json
import random
co = cohere.Client("rrwaMP5CuHu4lOQclEGvvY8dxcfGvOqcCesscCgy")

    
CUISINE_POSSIBILITIES = ["Italian", "Japanese", "Indian", "Mediterranean", "Thai", "Mexican", "Greek",
                         "Irish","Gastropub","Spanish", "European","Caribbean","Vietnamese","Steak House", 
                         "Bistro", "Chinese","Latin","French","Austrian","German","Indonesian","Dutch","Czech"]


def create_database(filename):
    fobj = open(filename, "w")
    rest_dict = {}
    for i in range(100):
        
        restaurant_name, menu = create_a_restaurant_dict()
        rest_dict[restaurant_name] = menu
        
    fobj.write(json.dumps(rest_dict))
    fobj.close()
        

def create_a_restaurant_dict():

    
    # pick a random cuisine
    number = random.randint(0,len(CUISINE_POSSIBILITIES)-1)
        
    # split via menu, strip spaces and colon
    restaurant_idea = generate_restaurant(CUISINE_POSSIBILITIES[number]).strip(" /n--")
        
    list_of_stuff = restaurant_idea.split("Menu: ")
        
    for j in range(len(list_of_stuff)):
        list_of_stuff[j] = list_of_stuff[j].strip()
        
    restaurant_name = list_of_stuff[0]
        
    menu = list_of_stuff[1].split(",")
        
    menu_dict = {}
        
    for item_price in menu:
        try:
            menu_list = item_price.strip().split(":")
                
            menu_dict[menu_list[0]] = float(menu_list[1].strip())
        except:
            continue
        
    return restaurant_name,menu_dict
            
            
        
        
    
    
    
    
def generate_restaurant(cuisine):
    prompt = f"""
    This program generates a restaurant name and a menu with a few items and a price for each given a cuisine.

    Cuisine: Italian
    Restaurant Name: Vitallia's
    Menu: Spaghetti:14.69,Garlic Bread:2.37,Lasagne:13.56
    --
    Cuisine : Sushi
    Restaurant Name: Paradise Rolls
    Menu: Salmon Rolls:9.00,Shrimp tempura:6.99,California Rolls:8.38
    --
    Cuisine: American
    Restaurant Name: Bob's Burgers
    Menu: Hamburger:5.00,Cheeseburger:9.00,Fries:4.99
    --
    Cuisine: Steakhouse
    Restaurant Name: The Keg
    Menu: Rare Steak:39.00,Caviar:150.00,Wine Reduction Roasted Pears:78.00
    --
    Cuisine: {cuisine}
    Restaurant Name: """

    response = co.generate(
        model='medium',
        prompt = prompt,
        max_tokens=40,
        temperature=0.6,
        stop_sequences=["--"])

    restaurant_idea = response.generations[0].text
    
    return restaurant_idea


if __name__ == "__main__":
    # create_database("fake_restaurants.json")
    
    fobj = open("fake_restaurants.json", "r")
    
    print(json.load(fobj))
    
    fobj.close()
    