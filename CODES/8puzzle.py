
from collections import deque

def solve(start, goal):
    queue = deque([(start, [])])
    visited = {tuple(start)}

    moves = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        zero = state.index(0)
        r, c = divmod(zero, 3)

        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr * 3 + nc
                new_state = state[:]
                new_state[zero], new_state[nz] = (
                    new_state[nz], new_state[zero]
                )

                key = tuple(new_state)

                if key not in visited:
                    visited.add(key)
                    queue.append(
                        (new_state, path + [state])
                    )

    return None


start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

result = solve(start, goal)

if result:
    for state in result:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution exists")
