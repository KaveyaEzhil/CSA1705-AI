
g = {
    'V1': [('V2', 9), ('V3', 4)],
    'V2': [('V1', 9), ('V3', 2), ('V4', 7), ('V5', 3)],
    'V3': [('V1', 4), ('V2', 2), ('V4', 4), ('V5', 6)],
    'V4': [('V2', 7), ('V3', 4), ('V5', 4), ('V6', 8)],
    'V5': [('V2', 3), ('V3', 6), ('V4', 4), ('V6', 2)],
    'V6': [('V4', 8), ('V5', 2)]
}

q = [(0, 'V1', ['V1'])]
v = []

while q:
    q.sort()
    cost, n, path = q.pop(0)

    if n in v:
        continue

    v.append(n)

    if n == 'V6':
        print("Path:", " -> ".join(path))
        print("Cost:", cost)
        break

    for i, w in g[n]:
        if i not in v:
            q.append((cost + w, i, path + [i]))
