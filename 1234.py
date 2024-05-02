n, m = map(int, input().split())


def dfs(x, c = 1):
    components[-1].append(x)
    used[x] = 1 if c % 2 != 0 else 2
    for to in g[x]:
        if used[to] == 0:
            dfs(to, c + 1)
        # else:
        #     if used[to] == used[c]:
        #         print("NO")
        #         break
        #     break




def dfs1(x):
    components[-1].append(x)
    used[x] = 1
    for to in g[x]:
        if used[to] == 0:
            dfs(to)


g = [[] for _ in range(n + 1)]
used = [0] * (n + 1)
components = []

for i in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

for i in range(1, n + 1):
    if used[i] == 0:
        components.append([])
        y = i
        dfs(i, y)

table1 = [i + 1 for i in range(1, n+1) if used[i] == 1]
print(used, table1)
