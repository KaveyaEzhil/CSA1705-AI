g = {
    0: [1, 3],
    1: [4, 5],
    3: [7, 6],
    4: [2],
    5: [],
    7: [],
    6: [],
    2: []
}

v = []
q = [0]

while q:
    n = q.pop(0)
    if n not in v:
        print(n, end=" ")
        v.append(n)
        for i in g[n]:
            if i not in v:
                q.append(i)