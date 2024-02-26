# Traveling salesman problem solver

Program designed to solve travelling salesman problem using dynamic programming method, which allows to efficiently calculate optimal paths using an iterative approach. The main idea of ​​the dynamic programming method is to break a complex problem into simpler subproblems, the solutions of which can be combined to obtain an optimal solution to the entire problem.

## Functionality

- **Dynamic Programming**: Utilizes dynamic programming to calculate the shortest path that visits each city exactly once and returns to the starting city;
- **Efficient Solution**: Provides an efficient solution to the Travelling Salesman Problem by breaking it down into subproblems;
- **Optimal Route**: Determines the optimal route for the salesman to minimize the total distance traveled and visually displays the result;
- **Input Flexibility**: Allows users to input a custom set of cities and their distances to find the best route;
- **Performance Analysis**: Solver offers valuable information about the execution speed of the algorithm based on the number of cities.

## How to Use

1. Input the number of cities and their distances into the program.
2. Run the program to calculate the optimal route for the salesman.
3. View the output to see the sequence in which the cities should be visited.
4. Explore different city configurations to observe to find out how fast the algorithm finds the shortest path using the dynamic programming method

## Installing

1. Clone git repository:
```
$ git clone https://github.com/Vladislav-Sharapa/traveling-salesman-problem-solver
```
2. Create virtual enviroment using following command:

```
$ python -m venv venv
```
3. Install Python packages specified in the 'requirements.txt':
```
$ pip install -r requirements.txt
```
> :heavy_exclamation_mark: Before running this command, make sure your virtual environment has been activated

## Getting started

To start the program run the script "main.py":
```
$ python src/main.py
```




