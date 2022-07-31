# 1388

from collections import deque

# graph = []
# n, m = map(int, input().split())
# for i in range(n):
#     graph.append(list(input()))

graph = [['-', '|', '|', '-', '-', '|'], ['|', '|', '|', '|', '|', '|'], ['|', '|', '|', '-', '|', '-'], ['-', '|', '|', '|', '|', '-'], ['|', '|', '|', '|', '-', '|'], ['|', '|', '-', '|', '|', '-']]
print(graph)

def bfs(graph, start, visit):
    que = deque([start])
    visit[start] = True
    while que:
        v = que.popleft()
        for i in graph[v]:
            for j in i:
                if j == 


from collections import deque

# graph = []
# n, m = map(int, input().split())
# for i in range(n):
#     graph.append(list(input()))

graph = [['-', '|', '|', '-', '-', '|'], ['|', '|', '|', '|', '|', '|'], ['|', '|', '|', '-', '|', '-'], ['-', '|', '|', '|', '|', '-'], ['|', '|', '|', '|', '-', '|'], ['|', '|', '-', '|', '|', '-']]
print(graph)

def bfs(graph, start, visit):
    que = deque([start])
    visit[start] = True
    while que:
        v = que.popleft()
        for i in graph[v]:
            for j in i:
                if j == 