import random
import numpy as np

# Define the distance matrix for 4 cities
distance_matrix = np.array
    ['Denver': {'Phoenix': 1319, 'San Francisco': 2011, 'Los Angeles': 1641, 'San Diego': 1738},
    'Phoenix': {'Denver': 1319, 'San Francisco': 1207, 'Los Angeles': 595, 'San Diego': 563},
    'San Francisco': {'Denver': 2011, 'Phoenix': 1207, 'Los Angeles': 611, 'San Diego': 804},
    'Los Angeles': {'Denver': 1641, 'Phoenix': 595, 'San Francisco': 611, 'San Diego': 193},
    'San Diego': {'Denver': 1738, 'Phoenix': 563, 'San Francisco': 804, 'Los Angeles': 193}]


# Parameters
population_size = 10
mutation_rate = 0.1
generations = 100

# Generate initial population
def generate_population(size, num_cities):
    return [random.sample(range(num_cities), num_cities) for _ in range(size)]

# Calculate fitness (total distance of the trip)
def fitness(individual, distance_matrix):
    return sum(distance_matrix[individual[i], individual[i + 1]] for i in range(len(individual) - 1)) + distance_matrix[individual[-1], individual[0]]

# Selection (tournament selection)
def selection(population, fitnesses):
    selected = random.choices(population, weights=[1/f for f in fitnesses], k=2)
    return selected

# Crossover (ordered crossover)
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

# Mutation (swap mutation)
def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(individual) - 1)
            individual[i], individual[j] = individual[j], individual[i]

# Genetic Algorithm
def genetic_algorithm(distance_matrix, population_size, mutation_rate, generations):
    num_cities = len(distance_matrix)
    population = generate_population(population_size, num_cities)
    for generation in range(generations):
        fitnesses = [fitness(ind, distance_matrix) for ind in population]
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = selection(population, fitnesses)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
    best_individual = min(population, key=lambda ind: fitness(ind, distance_matrix))
    return best_individual, fitness(best_individual, distance_matrix)

# Run the algorithm
best_trip, best_distance = genetic_algorithm(distance_matrix, population_size, mutation_rate, generations)
print(f"Best trip: {best_trip}")
print(f"Best distance: {best_distance}")