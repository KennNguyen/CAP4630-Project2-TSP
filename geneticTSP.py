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

def initRandCities(cityCount):
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

def queryUser(query, typeDesired, defaultValue = False):
    """Queries the user, for a specific type, can accept default value"""
    while(1):
        print(query, end = " ")
        userInput = input()
        try:

            if (len(userInput) == 0 and defaultValue):
                return defaultValue
            elif (typeDesired == "string"):
                return userInput
            elif (typeDesired == "int"):
                return int(userInput)
            elif (typeDesired == "float"):
                return float(userInput)
            elif (typeDesired == "bool"):
                if (userInput.lower() == "y"):
                    return True
                elif (userInput.lower() == "n"):
                    return False
        except ValueError:
            print("Please enter", typeDesired)

if __name__ == "__main__":
    print("Welcome to a Genetic Algorithm solver for  the TSP")

    cityCount = queryUser(("How many cities do you want? (Enter for default ("+ str(DEFAULT_CITY_COUNT) + ")) (int)"), "int", DEFAULT_CITY_COUNT)
    random_cities = initRandCities(cityCount)

    print("Cities generated!")
    printCities(random_cities)

    mutationRate = queryUser("What mutation rate do you want (float)?", "float")

    childProportion = queryUser("What proportion of new children do you want (float)? ", "float")

    stopOnStagnation = queryUser("Stop the algorithm on stagnation? (y/n)", "bool")

    whenIsStagnation = 0
    if(stopOnStagnation):
        whenIsStagnation = queryUser("How many iterations before stagnation is considered? (int)", "int")

    print("TEST: ", mutationRate, childProportion, stopOnStagnation, whenIsStagnation)

