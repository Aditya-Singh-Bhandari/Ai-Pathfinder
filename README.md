A* Pathfinding Agent
This repository contains a Python implementation of an Intelligent Agent that uses the A* Search Algorithm to find the shortest path in a dynamic grid environment. This project aligns with the Fundamentals in AI and ML (CSA2001) syllabus, specifically covering Problem Solving Methods and Informed Search Strategies.

Features

Informed Search: Implements the A* algorithm, utilizing a Manhattan distance heuristic for efficient pathfinding.


Dynamic Environments: Includes a grid generator that creates randomized obstacles, simulating the nature of stochastic environments.

Visual Output: Renders an ASCII-based representation of the grid, showing the start (S), goal (G), obstacles (#), and the calculated path (*).


Zero Dependencies: Uses only Python standard libraries like heapq and random.


How It Works:
The agent calculates the best path by minimizing the function:

f(n)=g(n)+h(n)
g(n): The actual cost from the start node to node n.


h(n): The heuristic estimated cost from node n to the goal, calculated using Manhattan distance.


f(n): The total estimated cost of the cheapest solution through node n.



References
Textbook: Russell, S., & Norvig, P. (2009). Artificial Intelligence: A Modern Approach. 
