g = {
    1: [2, 3],
    2: [5, 6],
    3: [4, 7],
    5: [],
    6: [],
    4: [8],
    7: [],
    8: []
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