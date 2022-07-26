# BOJ _ 연결 요소의 개수

# DFS _ 시간 초과

dic = {}
n, m = map(int, input().split())

for i in range(m):
    u, v = map(int, input().split())
    if u not in dic.keys():
        dic[u] = [v]
    else:
        dic[u].append(v)

# dic = {1: [2], 2: [5], 5: [1], 3: [4], 4: [6]}
# dic = {1: [2], 2: [5, 4, 3], 5: [1, 4], 3: [4], 4: [6]}

cnt = 0

for i in dic.items():
    for j in i[1]:
        if j in dic.keys():
            if len(dic[j]) != 0:
                for _ in range(len(dic[j])):
                    if dic[j] not in i[1]:
                        i[1].append(dic[j].pop())

for i in dic.values():
    if len(i) > 0:
        cnt += 1

print(cnt)


# BOJ _ 11724 _ bfs

from collections import deque 

def bfs(graph, v, visit):
    que = deque([v]) # 현재 노드의 연결 요소 계산
    visit[v] = True # 현재 노드 방문
    while que: # 현재 노드와 연결된 노드를 전부 확인할 때까지
        v = que.popleft() 
        for i in graph[v]: # 연결된 노드 중에서
            if not visit[i]: # 연결된 노드가 방문하지 않았다면
                que.append(i) # que에 다음 방문자로 지정(이 노드와 연결된 노드 확인하기 위해)
                visit[i] = True # 방문

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2) 
    graph[v2].append(v1) # 연결된 노드 저장
visit = [False] * (n + 1)
cnt = 0

for v in range(1, n + 1):
    if visit[v]: continue
    bfs(graph, v, visit)
    cnt += 1

print(cnt)