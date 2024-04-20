# Genetic Algorithm for Minimizing Linear Functions

This repository contains a Python genetic algorithm implementation for minimizing linear functions.

## Overview

Genetic algorithms are a class of optimization algorithms inspired by the process of natural selection. In this project, we apply a genetic algorithm to minimize linear functions.


## Features
- **Genetic Algorithm Implementation**: Utilizes a genetic algorithm approach to iteratively optimize the coefficients of the linear function.
- **Customizable Parameters**: Easily adjustable parameters such as population size, mutation rate, and selection criteria.
- **Efficient Optimization**: Efficiently minimizes linear functions to find optimal solutions.

## Getting Started
### Prerequisites
- Python 3.x

## Installation
1. Clone the repository:

```bash
git clone https://github.com/your-username/genetic-algorithm-linear-functions.git](https://github.com/kennethtegrado/linear-minimization-genetic-algorithm.git)
```
2. Navigate to the project directory:
```bash
cd linear-minimization-genetic-algorithm
```
## Usage
1. Modify the parameters in the `main.py` file to tune the inputs for the Genetic Algorithm.
2. Change the fitness function to control how the algorithm finds a solution.
3. Run `main.py` to execute the genetic algorithm.
```bash
python main.py
```
## Example

Here's an example of how to use the genetic algorithm to minimize a linear function:

```python
# Inside main.py

# modify the parameters
POPULATION = 100
GENERATIONS = 20
BINARY_LENGTH = 10
DECIMAL_PLACES = 2
VARIABLE_COUNT = 3
MIN_INTERVAL = -5.11
MAX_INTERVAL = 5.12
INTERVAL = 0.01

# fitness function where we base output on cost
def fitness_function(individual):
  # Minimize the sum of squares of the variables
  return sum([x**2 for x in individual])
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Inspired by the concept of genetic algorithms and optimization techniques.
- Prof. Jaderick Pabico from the University of the Philippines Los Baños.
