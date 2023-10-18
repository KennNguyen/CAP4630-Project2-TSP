Kenneth Nguyen(Reporter), Yurixander Silva(Architect), Zee Fisher(Developer)  
Professor Marques   
CAP 4630   
September 30, 2023  

# Traveling Salesman Problem using Genetic Algorithm Report 

## Work Report
At the beginning of the project, Kenneth done basic research on the what genetic algorithm is and how the implementation would be done for the Traveling Salesman Problem. Zee coded the basic program in which it gathers parameter information from the user and prints them out as well as the web side of the solution. Kenneth coded several function such as cities generation, distance calculation, and selection function. Yurixander coded the rest of the remaing functions of the genetic algorithm along with research and decisions on specificity of the functions such as selection method due to better selection of better fit parents than fitness proportionate selection.  

## Possible Improvements
There are many possible improvements to the code. To begin with we could have improved the crossover strategy using an advance crossover method such as order or cycle crossover. Moreover, the mutation rate can be improved as well with a more dynamic or adaptive mutation rate to where it has a higher mutation rate in the beginning, but slows down in later generations. In addition, we could have implemented heuristics seach algorithms to work along side the genetic algorithm such as opt search to refine solution quality. As well as that, process could be parallelized for exploration of multiple regions simultaneously for faster process or work alongside different optimization process such as simulated annealing, particle swarm optimization, or ant colony optimization. Finally, we could improve on stopping conditions with stagnation, fixed time limits, or with resource constraints.

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

Simple experiments that we ran on out program was alteration of values to see the change in final values such as the alteration of iterations to see if the computer can come up with a better route if given many iterations.
 
## Screenshots and .gifs
!["Original TSP solution"](https://github.com/KennNguyen/CAP4630-Project2-TSP/blob/main/images/tsp.gif?raw=true)

!["Web TSP solution"](https://github.com/KennNguyen/CAP4630-Project2-TSP/blob/main/images/wstsp.png?raw=true)

 
