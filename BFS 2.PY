g = {
    1: [2, 7],
    2: [3, 6],
    7: [8, 10],
    3: [4, 5],
    6: [9],
    8: [],
    10: [],
    4: [],
    5: [],
    9: []
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