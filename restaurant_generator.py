import cohere
import json
import random
co = cohere.Client("rrwaMP5CuHu4lOQclEGvvY8dxcfGvOqcCesscCgy")


cuisine_possibilities = ["Italian", "Japanese", "Indian", "Mediterranean", "Thai", "Mexican", "Greek",
                         "Irish","Gastropub","Spanish", "European","Caribbean","Vietnamese","Steak House", 
                         "Bistro", "Chinese","Latin","French","Austrian","German","Indonesian","Dutch","Czech"]


def create_restaurant_dict(filename):
    fobj = open(filename, "w")
    
    for i in range(100):
        
        # pick a random cuisine
        number = random.randint(len(cuisine_possibilities))
        
        # split via menu, strip spaces and colon
        restaurant_idea = generate_restaurant(cuisine_possibilities[number])
        
    
    
    
    
def generate_restaurant(cuisine):
    prompt = f"""
    This program generates a restaurant name and a menu with a few items and a price for each given a cuisine.

    Cuisine: Italian
    Restaurant Name: Vitallia's
    Menu: Spaghetti:14.69,Garlic Bread:2.37,Lasagne:13.56
    --
    Cuisine : Sushi
    Restaurant Name: Paradise Rolls
    Menu: Salmon Rolls: 9.00,Shrimp tempura:6.99,California Rolls:8.38
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


print(generate_restaurant(cuisine_possibilities[5]))