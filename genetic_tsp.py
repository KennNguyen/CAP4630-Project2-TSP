from typing import Optional
import random

City = tuple[str, float, float]
Point = tuple[float, float]

def generate_city_name(n: int) -> str:
    """Returns string name based on an int > 0."""
    name = "A" if n == 0 else ""

    while n > 0:
        name += chr(65 + (n % 26))
        n = int(n / 26)

    return name

def print_cities(cities: list[City]) -> None:
    print("{:6}\t{:>6}\t{:>6}".format("City", "X", "Y"))

    for city in cities:
        print("{:6}\t{:>6.2f}\t{:>6.2f}".format(city[0],city[1],city[2]))

def init_random_cities(count: int) -> list[City]:
    """Returns initialized list of random cities."""
    cities: list[City] = []
    max_x_axis = 200
    max_y_axis = 200

    for i in range(count):
        city_name = generate_city_name(i)
        x = random.uniform(0, max_x_axis)
        y = random.uniform(0, max_y_axis)
        cities.append((city_name, x, y))

    return cities

def calculate_distance(point1: Point, point2: Point) -> float:
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def fitness(cities: list[City]) -> float:
    total_distance = 0.0
    previous_city = None

    for city in cities:
        if previous_city is not None:
            total_distance += calculate_distance((previous_city[1], previous_city[2]), (city[1], city[2]))

        previous_city = city

    return total_distance

def ask_yes_no_question(question: str, default: bool = False) -> bool:
    """Asks a yes or no question and returns a boolean"""
    while True:
        print(question + " (y/n)", end = " ")
        userInput = input()

        if (len(userInput) == 0 and default):
            return default
        elif userInput.lower() == "y":
            return True
        elif userInput.lower() == "n":
            return False

def query_user(query: str, default: Optional[str] = None) -> str:
    """Queries the user for input and returns their response"""
    print(query, end = " ")

    user_input = input()
    user_did_not_input_anything = len(user_input) == 0

    if default is not None and user_did_not_input_anything:
        return default
    elif not user_did_not_input_anything:
        return user_input

    return query_user(query, default)

if __name__ == "__main__":
    print("Welcome to a Genetic Algorithm solver for  the TSP")

    DEFAULT_CITY_COUNT: int = 26
    cityCount = int(query_user("How many cities do you want?", str(DEFAULT_CITY_COUNT)))
    random_cities = init_random_cities(cityCount)

    print("Cities generated!")
    print_cities(random_cities)

    mutation_rate = float(query_user("What mutation rate do you want (float)?"))
    child_proportion = float(query_user("What proportion of new children do you want (float)?"))
    stop_on_stagnation = ask_yes_no_question("Stop the algorithm on stagnation?")
    when_is_stagnation = 0

    if stop_on_stagnation:
        when_is_stagnation = query_user("How many iterations before stagnation is considered? (int)", "int")

    print("TEST: ", mutation_rate, child_proportion, stop_on_stagnation, when_is_stagnation)
