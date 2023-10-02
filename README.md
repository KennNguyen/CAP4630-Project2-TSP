# Genetic algorithm to solve the travelling salesman problem -- Web Extra Credit

This is a genetic algorithm to solve the travelling salesman problem. It is written in Python 3 and uses the `matplotlib` library to plot the results on a `flask` webserver.

## Install

1. Download or clone the respository.
2. Install Python3.
3. Install python module `matplotlib` *
4. Install `flask` *
5. Run `genetic_tsp.py` with the `flask` webserver

*When installing python modules on a system with a dedicated package manager (ie most Linux distros), use a python virtual enviroment before installing a python module.

## Parameters

* `iterations`: The number of iterations to run the algorithm for. Each iteration represents a new generation.
* `k`: The number of individuals to select from the population.
* `city_count`: The number of cities to visit in the route. The cities are randomly generated.
* `population_size`: The number of individuals in every generation.
* `mutation_rate`: The probability that a new individual will be mutated. The value should a float be between `0` and `1`, representing a percentage.

## Pipeline

The pipeline is as follows:

1. Generate a random population of `n` individuals.
2. Calculate the fitness of each individual, based on the total distance of the route.
3. Select the best `k` individuals by sorting the population by its fitness and taking the first `k` individuals (i.e. the individuals with the lowest distance).
4. Create `n` new individuals by combining the best `k` individuals.
5. Mutate the new individuals, based on the `mutation_rate`.
6. Repeat from step 2 until the desired number of iterations has been reached. Ideally, the plot should gradually decrease in dinstance, and converge to a shape.

## Implementation

* Each individual is represented as a `Route`, which is a list of `City` tuples.
* The fitness of each individual is calculated as the total distance of the route.
