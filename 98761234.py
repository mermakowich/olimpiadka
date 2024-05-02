n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append([])

for i in range(n):
    g[i].append(input())

print(g)

for i in range(n):
    s = g[i][0]
    for k in s:
        g[i].append(k)

print(g)


def dfs(g, j1=0, j2=0):
    for i in range(n):
        for j in range(1, m + 1):
            if g[i][j] == "#":
                g[i][j] = "+"
                j1 = list(j)
                while g[i][j] == "#":
                    j += 1
                j2 = list(j-1)
                return j1, j2
print(dfs(g))
