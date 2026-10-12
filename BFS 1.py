g = {
    1: [2, 3, 4, 5],
    2: [1],
    3: [1],
    4: [1],
    5: [1]
}

v = []
q = [1]

while q:
    n = q.pop(0)
    if n not in v:
        print(n, end=" ")
        v.append(n)
        for i in g[n]:
            if i not in v:
                q.append(i)