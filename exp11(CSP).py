def is_safe(region, color, assignment, graph):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring(graph, colors, assignment, regions):
    if len(assignment) == len(regions):
        return True

    region = regions[len(assignment)]

    for color in colors:
        if is_safe(region, color, assignment, graph):
            assignment[region] = color

            if map_coloring(graph, colors, assignment, regions):
                return True

            del assignment[region]

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

assignment = {}
regions = list(graph.keys())

if map_coloring(graph, colors, assignment, regions):
    print("Color Assignment:")
    for region, color in assignment.items():
        print(region, "->", color)
else:
    print("No solution exists")
