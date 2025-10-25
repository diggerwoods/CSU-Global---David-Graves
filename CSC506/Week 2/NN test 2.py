import math

# Coordinates of the cities (latitude, longitude)
cities = {
    'Denver': (39.7392, -104.9903),
    'Kansas City': (39.0997, -94.5786),
    'San Diego': (32.7157, -117.1611),
    'Las Vegas': (36.1699, -115.1398)
}

def haversine(coord1, coord2):
    # Haversine formula to calculate the distance between two points on the Earth
    R = 6371  # Radius of the Earth in kilometers
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def nearest_neighbor(start, cities):
    unvisited = list(cities.keys())
    unvisited.remove(start)
    path = [start]
    total_distance = 0

    current_city = start
    while unvisited:
        nearest_city = min(unvisited, key=lambda city: haversine(cities[current_city], cities[city]))
        total_distance += haversine(cities[current_city], cities[nearest_city])
        path.append(nearest_city)
        current_city = nearest_city
        unvisited.remove(nearest_city)

    # Return to the starting city
    total_distance += haversine(cities[current_city], cities[start])
    path.append(start)

    return path, total_distance

# Starting city
start_city = 'Denver'
path, total_distance = nearest_neighbor(start_city, cities)

print("Path:", " -> ".join(path))
print(f"Total Distance: {total_distance:.2f} km")
