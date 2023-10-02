Kenneth Nguyen, Yurixander Silva, Zee Fisher  
Professor Marques   
CAP 4630   
September 30, 2023  

# Traveling Salesman Problem using Genetic Algorithm Report 

## Work Report
At the beginning of the project, Kenneth done basic research on the what genetic algorithm is and how the implementation would be done for the Traveling Salesman Problem. Zee coded the basic program in which it gathers parameter information from the user and prints them out as well as the web side of the solution. Kenneth coded several function such as cities generation, distance calculation, and selection function. Yurixander coded the rest of the remaing functions of the genetic algorithm along with research and decisions on specificity of the functions such as selection method due to better selection of better fit parents than fitness proportionate selection.  

## Answers to Questions
Data regarding cities were encapsulated into a tuple in which it holds information on its identification, x-coordinate, and y-coordinate within the plane dimension of two hundred by two hundred. Data regarding distances are encapsulated into a list. 

The solution space is not explicitly encoded and does not precompute all possible routes. It dynamically explores the solution space by manipulating routes and assessing their fitness.  

Handling the creation of the initial population was done by using the random uniform function within the random library of Python. They were placed on a two hundred by two hundred plane and encapsulated into a tuple. 

Computation of the fitness score was done by summating all the routes of all possible routes. The resulting array of route lengths was sorted from shortest to longest and the shortest routes became parents. 

The selection method we originally had was the fitness proportionate selection, but was decided that best fit would be better for the selection of parents due to it being better at choosing optimal parents.  

The crossover method we used is a partially matched crossover strategy. We create new offspring routes by exchanging a segment of cities between two parent routes while preserving the relative order of cities.  

The mutation method we used is swap mutation. Two cities are randomly swapped within an individual route to allow the algorithm to explore different routes. 

The repopulation of the next generation is done by combining the best-fit parents with the mutated offspring. 

The stopping condition we used was a limited number of iterations as defined by the user.
 

 
