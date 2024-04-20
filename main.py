from genetic_algorithm import genetic_algorithm

POPULATION = 100
GENERATIONS = 20
BINARY_LENGTH = 10
DECIMAL_PLACES = 2
VARIABLE_COUNT = 3
MIN_INTERVAL = -5.11
MAX_INTERVAL = 5.12
INTERVAL = 0.01


# fitness function
def fitness_function(individual):
  # Minimize the sum of squares of the variables
  return sum([x**2 for x in individual])


winner = genetic_algorithm(VARIABLE_COUNT, POPULATION, 0.1, GENERATIONS,
                           fitness_function, MIN_INTERVAL, MAX_INTERVAL,
                           INTERVAL, DECIMAL_PLACES, BINARY_LENGTH)
formatted_winner = " ".join(
  [f"x{i+1}: {val}" for i, val in enumerate(winner[0])])
print("\n==== FINISHED RESULTS ====")
print("BEST INDIVIDUAL: ", formatted_winner)
print("DNA: ", winner[1])
print("FITNESS SCORE: ", fitness_function(winner[0]))
print("===========================\n")
