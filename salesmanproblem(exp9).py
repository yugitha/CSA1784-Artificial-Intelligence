from itertools import permutations

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)
cities = list(range(n))

min_cost = float('inf')
best_path = None

for path in permutations(cities[1:]):
    current_path = (0,) + path
    cost = 0

    for i in range(n - 1):
        cost += graph[current_path[i]][current_path[i + 1]]

    cost += graph[current_path[-1]][0]

    if cost < min_cost:
        min_cost = cost
        best_path = current_path

print("Minimum Cost:", min_cost)
print("Best Path:", best_path + (0,))
