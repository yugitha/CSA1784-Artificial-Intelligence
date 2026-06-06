from collections import deque
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors

def solve_puzzle(initial, goal):
    queue = deque([(initial, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        state_tuple = tuple(map(tuple, current))

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        if current == goal:
            return path + [current]

        for neighbor in get_neighbors(current):
            queue.append((neighbor, path + [current]))

    return None

initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 0],
    [6, 7, 8]
]

solution = solve_puzzle(initial_state, goal_state)

if solution:
    print("Solution Found!\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No Solution Exists")
