
n, m = map(int, input().split())


def dfs(g, n):
    used = [-1] * (n+1)
    for i in range(1, n+1):
        if used[i] == -1:
            to = [i]
            used[i] = 0
            while to:
                v = to.pop()
                for u in g[v]:
                    if used[u] == -1:
                        to.append(u)
                        used[u] = 1 - used[v]
                    elif used[u] == used[v]:
                        return False, []

    t = [i for i in range(n) if used[i] == 0]
    return True, t


g = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)


var, t = dfs(g, n)

if var:
    print("YES")
    print(*t)
else:
    print("NO")