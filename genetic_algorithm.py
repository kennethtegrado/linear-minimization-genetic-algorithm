import random


# function to slice a string based on
def slice_gene(gene, variable_count):
  length = len(gene)
  part_length = length // variable_count
  remainder = length % variable_count

  result = []
  start = 0
  for i in range(variable_count):
    end = start + part_length
    if i < remainder:
      end += 1
    result.append(gene[start:end])
    start = end
  return result


# use this function to encode the value of number to binary string
def encode_gene(individual, min_interval, interval, binary_length):
  res = ""
  for strand in individual:
    res += bin(int(
      (strand - min_interval) // interval))[2:].rjust(binary_length, "0")
  return res


# use this function to decode_gene a binary string to a number
def decode_gene(binary_string, variable_count, min_interval, interval):
  individual = slice_gene(binary_string, variable_count)
  result = []
  for gene in individual:
    result.append(round((int(gene, 2) * interval) + min_interval, 2))

  return result


# generate an invididual based on the number of variables
def create_individual(variable_count, min_interval, max_interval,
                      decimal_places):
  # individual holder
  individual = []
  for i in range(variable_count):
    # Generate random values for each variable
    individual.append(
      round(random.uniform(min_interval, max_interval), decimal_places))
  return individual


# create population
def create_population(population_size, variable_count, min_interval,
                      max_interval, interval, decimal_places, binary_length):
  population = []
  for i in range(population_size):
    population.append(
      encode_gene(
        create_individual(variable_count, min_interval, max_interval,
                          decimal_places), min_interval, interval,
        binary_length))
  # return population
  return population


# solve for the fitness scores of an individual
def calculate_fitness(population, variable_count, fitness_function,
                      min_interval, interval):
  fitness_scores = []
  for individual in population:
    fitness_scores.append(
      fitness_function(
        decode_gene(individual, variable_count, min_interval, interval)))

  if min(fitness_scores) < 0:
    return [z - min(fitness_scores) + 1 for z in fitness_scores]

  return fitness_scores


# probabilistic method for getting the parent
def roulette_wheel_selection(population, fitness_scores):
  total_fitness = sum(fitness_scores)
  probabilities = [score / total_fitness for score in fitness_scores]
  selected_parents = []
  for i in range(len(population)):  # Select 2 parents
    spin = random.uniform(0, 1)
    cumulative_probability = 0
    for j, probability in enumerate(probabilities):
      cumulative_probability += probability
      if spin <= cumulative_probability:
        selected_parents.append(population[j])
        break
  return selected_parents


def three_point_crossover(parent1, parent2):
  """
    Performs three-point crossover on two parent strings and returns two offspring.
    """
  # Choose three random crossover points
  positions = sorted(random.sample(range(len(parent1)), 3))

  # Perform crossover
  offspring1 = parent1[:positions[0]] + parent2[positions[0]:positions[
    1]] + parent1[positions[1]:positions[2]] + parent2[positions[2]:]
  offspring2 = parent2[:positions[0]] + parent1[positions[0]:positions[
    1]] + parent2[positions[1]:positions[2]] + parent1[positions[2]:]

  return offspring1, offspring2


def mutation(individual, mutation_rate):
  # get the mutation point
  mutation_point = random.randint(0, len(individual) - 1)

  individual = list(individual)
  individual[mutation_point] = "1"
  # return mutated individual
  return "".join(individual)


def evolve_population(population, mutation_rate, variable_count,
                      fitness_function, min_interval, interval):
  fitness_scores = calculate_fitness(population, variable_count,
                                     fitness_function, min_interval, interval)

  new_population = []

  while len(new_population) < len(population):
    # Select two parents
    parent1 = random.choices(population, weights=fitness_scores)[0]
    parent2 = random.choices(population, weights=fitness_scores)[0]

    # Crossover the parents to create two offspring
    offspring1, offspring2 = three_point_crossover(parent1, parent2)

    # Mutate the offspring
    mutated_offspring1 = mutation(offspring1, mutation_rate)
    mutated_offspring2 = mutation(offspring2, mutation_rate)

    new_population.append(mutated_offspring1)
    new_population.append(mutated_offspring2)

  return new_population


# do the genetic algorithm
def genetic_algorithm(variable_count, population_size, mutation_rate,
                      generations, fitness_function, min_interval,
                      max_interval, interval, decimal_places, binary_length):
  population = create_population(population_size, variable_count, min_interval,
                                 max_interval, interval, decimal_places,
                                 binary_length)
  fitness_scores = calculate_fitness(population, variable_count,
                                     fitness_function, min_interval, interval)
  # Create an initial population
  population = roulette_wheel_selection(population, fitness_scores)

  for i in range(generations):
    # Evolve the population for one generation
    population = evolve_population(population, mutation_rate, variable_count,
                                   fitness_function, min_interval, interval)

    fitness_scores = calculate_fitness(population, variable_count,
                                       fitness_function, min_interval,
                                       interval)
    best_individual = decode_gene(
      population[fitness_scores.index(max(fitness_scores))], variable_count,
      min_interval, interval)
    formatted_individual = " ".join(
      [f"x{i+1}: {val}" for i, val in enumerate(best_individual)])
    # print best individual per generation
    print(f"Generation {i+1} (Best Individual):\n{formatted_individual}")
    print(
      f"DNA: {encode_gene(best_individual, min_interval, interval, binary_length)}\n"
    )

  # Calculate the fitness scores for the final population
  fitness_scores = calculate_fitness(population, variable_count,
                                     fitness_function, min_interval, interval)
  # Find the best individual in the final population
  best_individual = population[fitness_scores.index(max(fitness_scores))]
  decoded_individual = decode_gene(best_individual, variable_count,
                                   min_interval, interval)
  # return best individual
  return decoded_individual, encode_gene(decoded_individual, min_interval,
                                         interval, binary_length)
