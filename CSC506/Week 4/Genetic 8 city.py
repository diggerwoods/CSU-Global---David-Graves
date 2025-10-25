import random
import numpy as np
import time

# Starts timer for algorithm
start_time = time.time()

# Define the distance matrix for 8 cities
distance_matrix = np.array([
    [0, 557, 1726, 611, 830, 1765, 1366, 1631],  # Distances from Denver
    [557, 0, 1242, 1140, 1354, 1247, 857, 1095],  # Distances from Kansas City
    [1726, 1242, 0, 2180, 2338, 1255, 1184, 1097], # Distances from Miami
    [611, 1140, 2180, 0, 271, 2369, 1974, 2233],  # Distances from Las Vegas
    [830, 1354, 2338, 271, 0, 2590, 2193, 2448],  # Distances from Los Angeles
    [1765, 1247, 1255, 2369, 2590, 0, 399, 184], # Distances from Boston
    [1366, 857, 1184, 1974, 2193, 399, 0, 292], # Distances from Buffalo
    [1631, 1095, 1097, 2233, 2448, 184, 292, 0] # Distances from New York
])

# Parameters
population_size = 100
generations = 500
mutation_rate = 0.1

# Generate initial population
def generate_population(size, num_cities):
    return [random.sample(range(num_cities), num_cities) for _ in range(size)]

# Calculate fitness
def calculate_fitness(route):
    return sum(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1)) + distance_matrix[route[-1], route[0]]

# Selection
def selection(population):
    fitness_scores = [(route, calculate_fitness(route)) for route in population]
    fitness_scores.sort(key=lambda x: x[1])
    return [route for route, _ in fitness_scores[:len(fitness_scores) // 2]]

# Crossover
def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = parent1[start:end]
    pointer = 0
    for gene in parent2:
        if gene not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = gene
    return child

# Mutation
def mutate(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]

# Genetic Algorithm
def genetic_algorithm(num_cities, population_size, generations, mutation_rate):
    population = generate_population(population_size, num_cities)
    for _ in range(generations):
        selected_population = selection(population)
        next_generation = []
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(selected_population, 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            next_generation.append(child)
        population = next_generation
    best_route = min(population, key=calculate_fitness)
    return best_route, calculate_fitness(best_route)

# Run the algorithm
best_route, best_distance = genetic_algorithm(8, population_size, generations, mutation_rate)
print(f"Best route: {best_route}")
print(f"Total distance: {best_distance} miles")

# Finds the total time for algorithm and prints
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")