from collections import deque

def water_jug():
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print(x, y)

        if x == 2:
            print("Goal Reached")
            return

        states = [
            (4, y),
            (x, 3),
            (0, y),
            (x, 0),
            (x - min(x, 3-y), y + min(x, 3-y)),
            (x + min(y, 4-x), y - min(y, 4-x))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

water_jug()
