import cohere
import json
import random
co = cohere.Client("rrwaMP5CuHu4lOQclEGvvY8dxcfGvOqcCesscCgy")

    
CUISINE_POSSIBILITIES = ["Italian", "Japanese", "Indian", "Mediterranean", "Thai", "Mexican", "Greek",
                         "Irish","Gastropub","Spanish", "European","Caribbean","Vietnamese","Steak House", 
                         "Bistro", "Chinese","Latin","French","Austrian","German","Indonesian","Dutch","Czech", "Sushi", "Seafood", "Breakfast", "Burger", "Comfort", "Thaï"]


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
    Cuisine: Mexican
    Restaurant Name: Bocallido
    Menu: Cheese Tequenos:14.00,Cheese and plantain Tequenos:17.00,Cheese and Guava Tequenos:17.00
    --
    Cuisine: Seafood
    Restaurant Name: OFish
    Menu: Fried Pickles:10.00,Onion Rings:11.00,Crab Cake:14.00,Buffalo Shrimp:12.00
    --
    Cuisine: Breakfast
    Restaurant Name: Cacoa 70
    Menu: Black and White Waffle:16.50,Chocolate & Hazelnut Waffle:16.95,Illegal Chocolate Waffle:16.50
    --
    Cuisine: Burger
    Restaurant Name: Burger Bros
    Menu: Texas BBG Burge:16.99,Cheezy Cheetos Crunchy Chicken:16.99,BurgerPlexe Suprême:24.99,Special - Double (14oz) Cheese Burger with Beef Bacon:24.99,Special - Fish Burger:14.99,001. Classic Burger:15.99,002. Cheeseburger:16.99,003. Burger - BurgerBros Spécial:17.99,004. Cheesy Melt Burger: 16.99,005. Egg Burger: 16.99,006. Spicy Burger: 16.99,007. Smoked Burger: 17.99,008. Fried Mozzarella Burger: 17.99,Classic Poutine:7.99,BurgerBros Poutine:11.99,Chicken Poutine:9.99,Spicy Poutine:7.99,Italian Poutine (vegetarian):7.99
    --
    Cuisine: Comfort
    Restaurant Name: Maynard
    Menu: Breakfast Burrito:12.00,Breakfast Sandwich:12.00,Homemade Hashbrown:2.00,Nashville Tofu:15.00,Ranch Wrap: 15.00,Burger:15.00,Tacos:15.00,Poutine:10.00,Small Poutine:8.00,Mac&Cheez:14.00,Chili:6.00
    --
    Cuisine: Thaï
    Restaurant Name: Thaï Express
    Menu: Thai Sausage Fried Rice:12.98,Thai Sausage Wraps:5.99,Red Curry with Cauliflower Rice:14.98,Yellow Curry with Cauliflower Rice:14.98,General Curry on Cauliflower Rice:15.88,General Thai Beef with Cauliflower Rice:15.88,General Thairacha with Cauliflower Rice:15.88,Fried Chicken Dumplings:4.50,Crispy Imperial Roll:1.98,Small Mango Salad:6.00
    --
    Cuisine: Chinese
    Restaurant Name: Teochew Foodie
    Menu: Fatcarons:37.00,Chef's Basket:75.00,Shrimp Rice Noodle Roll:14.49,Meat Rice Noodle Rolls:12.49,Vegan Rice Noodle Rolls:12.49,Chicken & Shimeji Mushroom Wonton Soup:12.99,Pork & Shrimp Wonton Soup:12.99,Pork & Shrimp Steamed Wontons:12.99,Steamed Shrimp Wontons:14.99,Pork and Shrimp Fried Wontons:7.99,Teochew Vermicelli:7.99,Teochew Speciality Vinegar Dipping Sauce:4.99,Small Sauce Trio:3.99,Crispy Chili Oil - Original:13.99
    --
    Cuisine: Mexican
    Restaurant Name: M4 Burritos
    Menu: Carnitas Burrito:15.00,Barbacoa Burrito:16.00,Chicken Burrito:16.00,Veggie Burrito:15.45,Veggie Bowl:15.45,Barbacoa Bowl:15.00,Carnitas Bowl:15.00,Chicken Quesadilla:16.50,Veggie Quesadilla:15.95,Carnitas Quesadilla:15.50,Chicken Tacos:13.95,Tofu Tacos:12.95
    --
    Cuisine: Bistro
    Restaurant Name: Hooters
    Menu: Hooters Style Original Wings:12.99,Boneless Wings:13.99,Hooters Smoked Wings:13.99,Wing Ding Special:35.99,Fried Pickles:8.99,Lots a Tots:8.89,Cheese Sticks:8.99,Curly Fries:4.99,Chicken Quesadillas:11.99,Hooters Burger:12.99,Hooters Cheeseburger:13.99,Big hootie:16.99,Western BBQ burger:14.99,Vegetarian Burger:9.99,Hooters Buffalo Shrimp:12.99,Alaskan Snow Crab Legs:26.99,Garden Salad:9.99
    --
    Cuisine: {cuisine}
    Restaurant Name: """

    response = co.generate(
        model='medium',
        prompt = prompt,
        max_tokens=75,
        temperature=0.6,
        stop_sequences=["--"])

    restaurant_idea = response.generations[0].text
    
    return restaurant_idea


if __name__ == "__main__":
    create_database("newer_fake_restaurants.json")
    
    # fobj = open("new_fake_restaurants.json", "r")
    
    # print(json.load(fobj))
    
    # fobj.close()
    