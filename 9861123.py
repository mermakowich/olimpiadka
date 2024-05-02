import sys
sys.setrecursionlimit(100000)


n, m = map(int, input().split())
# g = [list(input()) for _ in range(n)]
g = [["."] * (m+2)]
for i in range(n):
    g.append(["."] + list(input()) + ["."])
g.append(["."] * (m+2))


used = [[False for _ in range(m+2)] for _ in range(n+2)]

s = 0



def dfs(i, j):
    used[i][j] = True
    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if not used[x+i][y+j] and g[x+i][y+j] == "#":
            dfs(x+i, y+j)








for i in range(1, n+1):
    for j in range(1, m+1):
        if not used[i][j] and g[i][j] == "#":
            s += 1
            dfs(i, j)


print(s)







# for i in range(n):
#     for j in range(m):
#         if gn[i][j] == 1 and not used[i][j]:
#             dfs(gn[i][j], i, j)
#         elif gn[i][j] == 2 and not used[i][j]:
#             used[i][j] = True
