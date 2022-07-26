# BOJ _ 24444 _ BFS
from collections import deque

n, m, r = map(int, input().split())

def bfs(graph, start, visited):
    global order
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        orderlst[v] = order
        order += 1
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
orderlst = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for q in graph:
    q.sort()

order = 1
bfs(graph, r, visited)
for i in range(1, n + 1):
    print(orderlst[i])