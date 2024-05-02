# Чтение входных данных
n, m = map(int, input().split())
# Создание списка смежности для графа неприязней
graph = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
print(graph)


# Функция проверки возможности рассадки ОВП
def check_seating_plan(graph, n):
    color = [-1] * n  # Список цветов вершин (-1 - не окрашена, 0 - белая, 1 - черная)
    for i in range(n):  # Перебор вершин графа
        if color[i] == -1:  # Если вершина не окрашена, начинаем обход в глубину
            stack = [i]
            color[i] = 0  # Окрашиваем вершину в белый цвет
            while stack:
                v = stack.pop()
                for u in graph[v]:
                    if color[u] == -1:  # Если соседняя вершина ещё не окрашена
                        stack.append(u)
                        color[u] = 1 - color[v]  # Окрашиваем её в противоположный цвет
                    elif color[u] == color[v]:  # Если соседняя вершина окрашена в тот же цвет
                        return False, []  # Рассадка невозможна
    # Формируем список вершин, которые необходимо посадить за первый стол
    table1 = [i + 1 for i in range(n) if color[i] == 0]
    return True, table1


# Проверяем возможность рассадки ОВП и выводим результат
possible, table1 = check_seating_plan(graph, n)
if possible:
    print("YES")
    print(*table1)
else:
    print("NO")