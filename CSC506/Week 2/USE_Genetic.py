import random
import numpy as np

# Distance matrix (example distances in km)
distance_matrix = np.array([
    [0, 557, 611, 830],  # Distances from Denver
    [557, 0, 1140, 1354],  # Distances from Kansas City
    [611, 1140, 0, 271],  # Distances from Las Vegas
    [830, 1354, 271, 0],  # Distances from Los Angeles
])

# Parameters
population_size = 100
generations = 500
mutation_rate = 0.01

# Create initial population
def create_population(size, num_nodes):
    population = []
    for _ in range(size):
        individual = list(np.random.permutation(num_nodes))
        population.append(individual)
    return population

# Calculate fitness
def calculate_fitness(individual):
    total_distance = 0
    for i in range(len(individual) - 1):
        total_distance += distance_matrix[individual[i], individual[i + 1]]
    total_distance += distance_matrix[individual[-1], individual[0]]  # Return to start
    return 1 / total_distance

# Selection
def selection(population, fitnesses):
    selected = random.choices(population, weights=fitnesses, k=2)
    return selected

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
def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]

# Genetic Algorithm
def genetic_algorithm():
    num_nodes = len(distance_matrix)
    population = create_population(population_size, num_nodes)
    best_individual = None
    best_fitness = 0

    for generation in range(generations):
        fitnesses = [calculate_fitness(ind) for ind in population]
        new_population = []

        for _ in range(population_size // 2):
            parent1, parent2 = selection(population, fitnesses)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

        current_best_fitness = max(fitnesses)
        if current_best_fitness > best_fitness:
            best_fitness = current_best_fitness
            best_individual = population[fitnesses.index(current_best_fitness)]

    best_distance = 1 / best_fitness
    return best_individual, best_distance

# Run the algorithm
best_path, best_distance = genetic_algorithm()
print(f"Best path: {best_path}")
print(f"Shortest distance: {best_distance:.2f} km")
