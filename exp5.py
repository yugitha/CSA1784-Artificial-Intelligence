from collections import deque
def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False

    return True

def solve():
    start = (3, 3, 1)  
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        m, c, boat = state

        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for dm, dc in moves:
            if boat == 1:  
                new_state = (m-dm, c-dc, 0)
            else:          
                new_state = (m+dm, c+dc, 1)

            nm, nc, _ = new_state

            if is_valid(nm, nc):
                queue.append((new_state, path + [state]))

    return None


solution = solve()

print("Solution Path:")
for step in solution:
    print(step)
