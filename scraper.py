import json
import requests

def create_restaurant_dict(filename: str):
    restaurant_dict = {}
    
    fobj = open(filename, "r")
    
    contents = fobj.read().split("\n").split(",")
    
    for line in contents:
        restaurant_name = line[0]