
def sort(g):
    n = len(g)
    used = [False] * n
    trans = [False] * n
    res = []

    def dfs(i):
        if trans[i]:
            return False
        trans[i] = True
        for j in g[i]:
            if not used[j] and not dfs(j):
                return False
        trans[i] = False
        used[i] = True
        res.append(i)
        return True

    for i in range(n):
        if not used[i] and not dfs(i):
            return None
    return res


n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[b - 1].append(a - 1)
res = sort(g)

if res is None:
    print("No")
else:
    print("Yes")
    print(*(i + 1 for i in res))
