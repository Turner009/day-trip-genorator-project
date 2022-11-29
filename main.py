# day trip genorator project

import random

cities = ["New York", "Chicago", "San Francisco", "Vicksburg, MS"]
restaurants = ["Dallas BBQ", "Time Out Market", "Waffle House", "International Food Court"]
transportation = ["Uber", "Cycling", "Walking", "Rent a Car"]
entertainment = ["Museum Circuit", "Live Show Circuit", "Interactive Popup Circuit", "1 Museum, 1 Live Show, 1 Interactive Popup"]
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
        print(f"Your new city selection is", trip_selections["city"],".")
        city_answer = input("Do you like this choice? (Y or N)")
    print(f"Your confirmed city choice is",trip_selections["city"], ".")


def food():
    trip_selections["food"] = random.choice(restaurants)
    print("Your lunch will be from", trip_selections["food"],".")
    food_answer = input("Do you like this choice? (Y or N)")
    if food_answer == "Y":
        print("Confirmed")
    while food_answer == "N":
        trip_selections["food"] = random.choice(restaurants)
        print(f"Your new food selection is", trip_selections["food"],".")
        food_answer = input("Do you like this choice? (Y or N)")
    print(f"Your confirmed food choice is", trip_selections["food"], ".")



def transport():
    trip_selections["transportation"] = random.choice(transportation)
    print("Your transportation will be", trip_selections["transportation"],".")
    ride_answer = input("Do you like this choice? (Y or N)")
    if ride_answer == "Y":
        print("Confirmed")
    while ride_answer == "N":
        trip_selections["transportation"] = random.choice(transportation)
        print(f"Your new transportation selection is", trip_selections["transportation"],".")
        ride_answer = input("Do you like this choice? (Y or N)")
    print(f"Your confirmed transportation option is", trip_selections["transportation"], ".")

def entertain():
    trip_selections["entertainment"] = random.choice(entertainment)
    print(f"Your entertainment will be", trip_selections["entertainment"],".")
    entertain_answer = input("Do you like this choice? (Y or N)")
    if entertain_answer == "Y":
        print("Confirmed")
    while entertain_answer == "N":
        trip_selections["etertainment"] = random.choice(entertainment)
        print(f"Your new entertainment selection is", trip_selections["etertainment"],".")
        entertain_answer = input("Do you like this choice? (Y or N)")
    print(f"Your confirmed entertainment option is", trip_selections["etertainment"], ".")

# city()
# food()
# transport()
entertain()



 


    



