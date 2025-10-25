import random
def nearest_neighbor(distances):
    """
    Implements the Nearest Neighbor algorithm for the TSP.

    Args:
        distances: A 2D list/matrix representing the distances between cities.
                   distances[i][j] is the distance from city i to city j.

    Returns:
        A list representing the order of cities in the tour.
    """

    num_cities = len(distances)
    tour = []
    visited = set()
    current_city = random.randint(0, num_cities - 1)  # Start at a random city
    tour.append(current_city)
    visited.add(current_city)

    while len(visited) < num_cities:
        nearest_city = None
        min_distance = float('inf')

        for i in range(num_cities):
            if i not in visited:
                distance = distances[current_city][i]
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = i

        tour.append(nearest_city)
        visited.add(nearest_city)
        current_city = nearest_city

    return tour

# Add actual Distance for Broncos games amongst AFC West
# More Complex add distance for Broncos games amongst AFC
# More Complex add distance for Broncos games amongst NFL
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
tour = nearest_neighbor(distances)
print("Tour:", tour)