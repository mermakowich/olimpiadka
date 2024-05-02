def toposort(graph):
    n = len(graph)
    visited = [False] * n
    traversed = [False] * n
    result = []

    def traverse(i):
        if traversed[i]:
            return False
        traversed[i] = True
        for j in graph[i]:
            if not visited[j] and not traverse(j):
                return False
        traversed[i] = False
        visited[i] = True
        result.append(i)
        return True

    for i in range(n):
        if not visited[i] and not traverse(i):
            return None
    return result


def main():
    n, m = map(int, input().split())
    graph = tuple([] for _ in range(n))
    for _ in range(m):
        i, j = map(lambda w: int(w) - 1, input().split())
        graph[j].append(i)
    print(graph)
    result = toposort(graph)
    if result is None:
        print('No')
    else:
        print('Yes')
        print(*(i + 1 for i in result))


main()