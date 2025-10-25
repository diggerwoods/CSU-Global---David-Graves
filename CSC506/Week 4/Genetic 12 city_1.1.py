import random
import numpy as np
import time

# Starts timer for algorithm
start_time = time.time()

# Define the distance matrix for 12 cities
distance_matrix = np.array([
    [0, 557, 1726, 611, 830, 1765, 1366, 1631, 1463, 1020, 878, 998],  # Distances from Denver
    [557, 0, 1242, 1140, 1354, 1247, 857, 1095, 949, 472, 646, 451],  # Distances from Kansas City
    [1726, 1242, 0, 2180, 2338, 1255, 1184, 1097, 328, 817, 967, 1027], # Distances from Miami
    [611, 1140, 2180, 0, 271, 2369, 1974, 2233, 1966, 1576, 1225, 1590],  # Distances from Las Vegas
    [830, 1354, 2338, 271, 0, 2590, 2193, 2448, 2143, 1776, 1370, 1805],  # Distances from Los Angeles
    [1765, 1247, 1255, 2369, 2590, 0, 399, 184, 1017, 941, 1603, 805], # Distances from Boston
    [1366, 857, 1184, 1974, 2193, 399, 0, 292, 880, 626, 1285, 434], # Distances from Buffalo
    [1631, 1095, 1097, 2233, 2448, 184, 292, 0, 835, 758, 1417, 643], # Distances from New York
    [1463, 949, 328, 1966, 2143, 1017, 880, 835, 0, 499, 820, 699],  # Distances from Jacksonville
    [1020, 472, 817, 1576, 1776, 941, 626, 758, 499, 0, 665, 251],  # Distances from Nashville
    [878, 646, 967, 1225, 1370, 1603, 1285, 1417, 820, 665, 0, 865],  # Distances from Houston
    [998, 451, 1027, 1590, 1805, 805, 434, 643, 699, 251, 865, 0]  # Distances from Indianapolis
])

# Parameters
population_size = 100
generations = 250
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
best_route, best_distance = genetic_algorithm(12, population_size, generations, mutation_rate)
print(f"Best route: {best_route}")
print(f"Total distance: {best_distance} miles")

# Finds the total time for algorithm and prints
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")