#geneticTSP.py

import random

DEFAULT_CITY_COUNT: int = 26

def genCityName(n):
    """Returns string name based on an int > 0."""
    name = "A" if n == 0 else ""
    while(n > 0):
        name += chr(65 + (n % 26))
        n = int(n / 26)
    return name

def printCities(cities):
    """Prints a list of cities to Console"""
    print("{:6}\t{:>6}\t{:>6}".format("City", "X", "Y"))
    for city in cities:
        print("{:6}\t{:>6.2f}\t{:>6.2f}".format(city[0],city[1],city[2]))

def initRandCities(cityCount = DEFAULT_CITY_COUNT):
    """Returns initialized list of random cities."""
    cities = []
    max_x_axis = 200
    max_y_axis = 200
    for i in range(cityCount):
        city_name = genCityName(i)
        x = random.uniform(0, max_x_axis)
        y = random.uniform(0, max_y_axis)
        cities.append((city_name, x, y))
    return cities

if __name__ == "__main__":
    print("Welcome to a Genetic Algorithm solver for  the TSP")
    while(1):
        print("How many cities do you want? (Enter for default (", DEFAULT_CITY_COUNT ,")): ", sep = "" , end = "")
        userCityCount = input()
        if (userCityCount.isdigit()):
            random_cities = initRandCities(int(userCityCount))
            break
        elif (len(userCityCount) == 0):
            random_cities = initRandCities()
            break
    printCities(random_cities)

