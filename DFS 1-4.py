
def dfs(g, n, v):
    if n not in v:
        print(n, end=" ")
        v.append(n)

        for i in g[n]:
            dfs(g, i, v)


# 1st question
g = {
    1: [2, 3, 4, 5],
    2: [1],
    3: [1],
    4: [1],
    5: [1]
}
dfs(g, 1, [])
print()

# 2nd question
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
dfs(g, 1, [])
print()

# 3rd question
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
dfs(g, 1, [])
print()

# 4th question
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
dfs(g, 0, [])
print()
