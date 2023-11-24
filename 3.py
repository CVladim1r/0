from collections import defaultdict

def dfs(node, parent, xor_prefix, count_reachable):
    count_reachable[node] = 1

    # Обновляем xor_prefix для текущего города
    xor_prefix ^= edges[node]

    # Увеличиваем количество достижимых городов для всех городов,
    # у которых xor_prefix равен текущему значению.
    count_reachable[node] += count_reachable_by_prefix[xor_prefix]

    # Рекурсивно вызываем dfs для всех соседних городов, исключая родительский.
    for neighbor in graph[node]:
        if neighbor != parent:
            dfs(neighbor, node, xor_prefix, count_reachable)

    # Увеличиваем количество достижимых городов для текущего xor_prefix.
    count_reachable_by_prefix[xor_prefix] += 1

# Чтение входных данных
n = int(input())
graph = defaultdict(list)
edges = {}
count_reachable = [0] * (n + 1)
count_reachable_by_prefix = defaultdict(int)

# Заполняем граф и веса ребер
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    edges[v] = edges[u] ^ w

# Запускаем DFS из корня дерева (можно выбрать любой город в качестве корня)
dfs(1, 0, 0, count_reachable)

# Выводим результат
print(*count_reachable[1:])
