# PRESENTATION EXERCISE 2
# SEPTEMBER 23, 2022
# Authors: Nancy Gong and Rashmi Hemrajani

import math

def maximum_number_of_people():
    
    # Converting dimensions in cm to m:
    width_of_room = float(input("Enter width (in cm): ")) / 100
    length_of_room = float(input("Enter length (in cm): ")) / 100
    
    # Finding area of the room:
    area_room = (width_of_room*length_of_room)
    
    # Making sure width_of_room is the smaller side of the rectangle/room:
    if width_of_room > length_of_room:
        temp_variable = length_of_room
        length_of_room = width_of_room
        width_of_room = temp_variable
    
    # Making sure the inputs give a room:
    if width_of_room > 0 and length_of_room > 0:
    
        # Conditions for the expected exceptions:
        if width_of_room < 2 and length_of_room < 2:  # Can only fit 1 person (1 quarter circle)
            quarter_circles = 1
            half_circles = 0
            full_circles = 0
        
        elif width_of_room < 2 and length_of_room < 4:  # Can only fit a row of 2 quarter circles
            quarter_circles = 2
            half_circles = 0
            full_circles = 0
            
        elif width_of_room < 4 and length_of_room < 4: # Can only fit 4 quarter circles in each corner
            quarter_circles = 4
            half_circles = 0
            full_circles = 0
            
        elif width_of_room < 2 and length_of_room >= 4:  # Can only fit a row of 2 quarter circles and x amount of half circles
            quarter_circles = 2
            half_circles = (length_of_room-2) // 2    
            full_circles = 0
            
        else:
            quarter_circles = 4 
            
            # Finding dimensions of interior rectangle without people against walls or corners:
            width_of_interior_rectangle = ((width_of_room - 2) // 2) * 2
            length_of_interior_rectangle = ((length_of_room - 2) // 2) * 2
            
            # Ensuring there are no negative intergers:
            if width_of_interior_rectangle < 0:
                width_of_interior_rectangle = 0
                
            if length_of_interior_rectangle < 0:
                length_of_interior_rectangle = 0
           
            # Finding how many people against walls:
            half_circles = width_of_interior_rectangle + length_of_interior_rectangle
            
            # Finding how many people fit in the middle (full circles):
            width_of_rectangle_for_full_circles = width_of_interior_rectangle // 2
            length_of_rectangle_for_full_circles = length_of_interior_rectangle // 2
            full_circles = (width_of_rectangle_for_full_circles * length_of_rectangle_for_full_circles)
    
        # Determining maximum amount of people in the room:  
        max_number_of_people = quarter_circles + half_circles + full_circles

        # Determining maximum and minimum percentage of available space for each person:
        area_of_unit_circle = math.pi * (1 ** 2)
        minimum = ((area_of_unit_circle/4)/area_room) * 100

        if quarter_circles == 1:
            minimum = 100
            maximum = minimum
        elif full_circles > 0:
            maximum = minimum * 4
        elif half_circles > 0:
            maximum = minimum * 2
        else:
            maximum = minimum
           
           
        print("There can be a maximum of ", max_number_of_people,"people in this room.")
        print("Each needing no less than",round(minimum,3),"% and no more than",(round(maximum,3)),"% of the available surface to maintain a 2 meter distance.")


    else:
        print("A classroom of", width_of_room, "m by ", length_of_room, "m does not exist.")



