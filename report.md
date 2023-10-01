Kenneth Nguyen, Yurixander Silva, Zee Fisher  
Professor Marques   
CAP 4630   
September 30, 2023  

# Traveling Salesman Problem using Genetic Algorithm Report 

Design Answer To Questions 

Data regarding cities were encapsulated into a tuple in which it holds information on its identification, x-coordinate, and y-coordinate within the plane dimension of two hundred by two hundred. Data regarding distances are encapsulated into a list or an array for processing. 

The solution space is not explicitly encoded and does not precompute all possible routes, but it dynamically explores the solution space by manipulating routes and assessing their fitness.  

Handling of the creation of the initial population was done by using the random uniform function within the random library of Python within a two hundred by two hundred plane and having it encapsulated into a tuple. 

Computation of the fitness score was done by summating all the routes of all possible routes and having the array sorted from least to most and choosing the shortest route to become parents. 

The selection method we originally had was the roulette selection, but was decided that best fit would be better for the selection of parents due to it being better when choosing better parents.  

The crossover method we used is a partially matched crossover strategy in which we create new offspring routes by exchanging a segment of cities between two parent routes while preserving the relative order of cities.  

The mutation method we used is swap mutation in which two cities are randomly swapped within an individual route to allow the algorithm to explore different routes. 

The repopulation of the next generation is done by combining the best-fit parents with the mutated offspring. 

The stopping condition we used was the number of iterations defined by the user.  

 

 
