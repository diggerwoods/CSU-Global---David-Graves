import random
import numpy as np

# Distance matrix (example values, replace with actual distances)
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
generations = 500
mutation_rate = 0.01

def create_route():
    route = list(range(1, len(distance_matrix)))
    random.shuffle(route)
    return [0] + route + [0]

def create_population(size):
    return [create_route() for _ in range(size)]

def fitness(route):
    return sum(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))

def selection(population):
    population.sort(key=lambda x: fitness(x))
    return population[:population_size // 2]

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [-1] * len(parent1)
    child[start:end] = parent1[start:end]
    for city in parent2:
        if city not in child:
            for i in range(len(child)):
                if child[i] == -1:
                    child[i] = city
                    break
    return child

def mutate(route):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(route) - 1), 2)
        route[i], route[j] = route[j], route[i]

def genetic_algorithm():
    population = create_population(population_size)
    for _ in range(generations):
        selected = selection(population)
        children = []
        for i in range(len(selected) // 2):
            parent1, parent2 = selected[i], selected[-i - 1]
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1)
            mutate(child2)
            children.extend([child1, child2])
        population = selected + children
    best_route = min(population, key=lambda x: fitness(x))
    return best_route, fitness(best_route)

best_route, best_distance = genetic_algorithm()
print("Best route:", best_route)
print("Best distance:", best_distance)