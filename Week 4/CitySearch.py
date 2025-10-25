from simpleai.search import SearchProblem, astar

# Define the cities and their connections (edges with distances)
city_map = {
    'Denver': {'Chicago': 1000, 'Houston': 1050, 'Nashville': 1020},
    'Chicago': {'Denver': 1000, 'Nashville': 470, 'Miami': 1370},
    'Houston': {'Denver': 1050, 'Miami': 1190, 'Nashville': 670},
    'Miami': {'Houston': 1190, 'Chicago': 1370, 'Nashville': 910},
    'Nashville': {'Denver': 1020, 'Chicago': 470, 'Houston': 670, 'Miami': 910},
}

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
        # Simple heuristic: straight-line distance (use direct edge if exists, else 0)
        return city_map[state].get(self.goal, 0)

def main():
    print("Available cities:", ', '.join(cities))
    start = input("Enter start city: ").strip().title()
    goal = input("Enter goal city: ").strip().title()

    if start not in cities or goal not in cities:
        print("Invalid city name(s).")
        return

    problem = CityProblem(start, goal)
    result = astar(problem)

    print("\nPath from {} to {}:".format(start, goal))
    for step, (action, state) in enumerate(result.path()):
        if action is not None:
            print(f"{step}: {action} -> {state}")
        else:
            print(f"{step}: Start at {state}")
    print(f"Total cost: {result.cost}")

if __name__ == "__main__":
    main()
