n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(m, count):
    if m == end:
        return count

    visited[m] = True

    for n in graph[m]:
        if not visited[n]:
            result = dfs(n, count + 1)
            if result is not None: 
                return result
    return None

result = dfs(start, 0)
if result is not None:
    print(result)
else:
    print(-1)
