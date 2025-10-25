from simpleai.search import SearchProblem, astar
from math import radians, sin, cos, sqrt, atan2

# City coordinates (latitude, longitude)
city_coords = {
    'Denver': (39.7392, -104.9903),
    'Chicago': (41.8781, -87.6298),
    'Houston': (29.7604, -95.3698),
    'Miami': (25.7617, -80.1918),
    'Nashville': (36.1627, -86.7816),
    'Los Angeles': (34.0522, -118.2437),
    'London': (51.5074, -0.1278),
    'Paris': (48.8566, 2.3522),
}

city_map = {
    'Denver':    {'Chicago': 1000, 'Houston': 1050, 'Nashville': 1020, 'Los Angeles': 1015},
    'Chicago':   {'Denver': 1000, 'Nashville': 470, 'Miami': 1370, 'London': 3950},
    'Houston':   {'Denver': 1050, 'Miami': 1190, 'Nashville': 670, 'Los Angeles': 1550},
    'Miami':     {'Houston': 1190, 'Chicago': 1370, 'Nashville': 910, 'London': 4420, 'Paris': 4560},
    'Nashville': {'Denver': 1020, 'Chicago': 470, 'Houston': 670, 'Miami': 910, 'Los Angeles': 2000},
    'Los Angeles': {'Denver': 1015, 'Houston': 1550, 'Nashville': 2000, 'London': 5450, 'Paris': 5650},
    'London':    {'Chicago': 3950, 'Miami': 4420, 'Los Angeles': 5450, 'Paris': 215},
    'Paris':     {'Miami': 4560, 'Los Angeles': 5650, 'London': 215},
}

def haversine(coord1, coord2):
    # Calculate the great-circle distance between two points (in miles)
    R = 3958.8  # Earth radius in miles
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

cities = list(city_map.keys())

class CityProblem(SearchProblem):
    def __init__(self, initial, goal):
        super().__init__(initial_state=initial)
        self.goal = goal

    def actions(self, state):
        return list(city_map[state].keys())

    def result(self, state, action):
        return action

    def is_goal(self, state):
        return state == self.goal

    def cost(self, state, action, state2):
        return city_map[state][action]

    def heuristic(self, state):
        # Use straight-line (haversine) distance as heuristic
        return haversine(city_coords[state], city_coords[self.goal])

def main():
    print("Available cities:", ', '.join(cities))
    start = input("Enter start city: ").strip().title()
    goal = input("Enter goal city: ").strip().title()

    if start not in cities or goal not in cities:
        print("Invalid city name(s).")
        return

    problem = CityProblem(start, goal)
    result = astar(problem)

    print(f"\nPath from {start} to {goal}:")
    path = result.path()
    for i in range(len(path) - 1):
        old_city = path[i][1]
        new_city = path[i + 1][1]
        print(f"{i}: {old_city} -> {new_city}")
    print(f"Total cost: {result.cost}")

if __name__ == "__main__":
    main()