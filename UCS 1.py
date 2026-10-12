
g = {
    'S': [('A', 1), ('G', 12)],
    'A': [('B', 3), ('C', 1)],
    'B': [('D', 3)],
    'C': [('D', 1), ('G', 2)],
    'D': [('G', 3)],
    'G': []
}

q = [(0, 'S', ['S'])]
v = []

while q:
    q.sort()
    cost, n, path = q.pop(0)

    if n in v:
        continue

    v.append(n)

    if n == 'G':
        print("Path:", " -> ".join(path))
        print("Cost:", cost)
        break

    for i, w in g[n]:
        if i not in v:
            q.append((cost + w, i, path + [i]))
