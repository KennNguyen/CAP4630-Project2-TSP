# Genetic algorithm to solve the travelling salesman problem

This is a genetic algorithm to solve the travelling salesman problem. It is written in Python 3 and uses the `matplotlib` library to plot the results.

## Pipeline

The pipeline is as follows:

1. Generate a random population of `n` individuals
2. Calculate the fitness of each individual
3. Select the best `k` individuals
4. Create `n` new individuals by combining the best `k` individuals
5. Mutate the new individuals
6. Repeat from step 2 until the best individual has converged
