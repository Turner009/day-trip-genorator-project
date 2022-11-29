# day trip genorator project

import random

cities = ["New York", "Chicago", "San Francisco", "Vicksburg, MS"]
restaurants = ["Dallas BBQ", "Time Out Market", "Waffle House", "International Food Court"]
transportation = ["Uber", "Cycling", "Walking", "Rent a Car"]
entertanment = ["Museum Circuit", "Live Show Circuit", "Interactive Popup Circuit", "1 Museum, 1 Live Show, 1 Interactive Popup"]
trip_selections = {"city":"", "food":"", "transportation":"", "entertainment":""}

print("Welcome to the day trip genorator! Let get started.")

def city():
    trip_selections["city"] = random.choice(cities)
    print("You will be traveling to", trip_selections["city"],".")
    city_answer = input("Do you like this choice? (Y or N)")
    if city_answer == "Y":
        print("Confirmed")
    while city_answer == "N":
        trip_selections["city"] = random.choice(cities)
        print(f"New selection is", trip_selections["city"],".")
        city_answer = input("Do you like this choice? (Y or N)")
    print(f"Your confirmed city choice is",trip_selections["city"], ".")
             
city()


    



