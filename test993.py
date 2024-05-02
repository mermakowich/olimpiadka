import sys
from collections import deque

max_size = 100 + 5
n, m = 0, 0
mas = [[''] * max_size for _ in range(max_size)]

def input_data():
    global n, m
    n, m = map(int, input().split())
    for i in range(n):
        line = input()
        for j in range(m):
            mas[i][j] = line[j]

def correct(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x, y):
    move_x = [0, 1, 0, -1]
    move_y = [1, 0, -1, 0]
    queue = deque([(x, y)])
    mas[x][y] = '.'
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            new_x, new_y = cur_x + move_x[i], cur_y + move_y[i]
            if correct(new_x, new_y) and mas[new_x][new_y] == '#':
                queue.append((new_x, new_y))
                mas[new_x][new_y] = '.'

def solve():
    amount = 0
    for i in range(n):
        for j in range(m):
            if mas[i][j] == '#':
                bfs(i, j)
                amount += 1
    print(amount)

if __name__ == "__main__":
    input_data()
    solve()

