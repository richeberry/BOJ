# BOJ _ 큐 2


import sys
from collections import deque

input = sys.stdin.readline
q = deque() 

for _ in range(int(input())):
    a = input().split()
    if 'push' == a[0]: # push _ 수를 queue에 더함
        q.append(a[1])

    elif 'front' == a[0]: # front _ queue가 비어있으면 -1 출력, 아니면 top 출력
        if not q: print(-1)
        else:
            print(q[0])

    elif 'back' == a[0]: # back _ queue가 비어있으면 -1 출력, 아니면 bottom 출력
        if not q: print(-1)
        else:
            print(q[-1])

    elif 'size' == a[0]: # size _ queue의 사이즈 출력
        print(len(q))

    elif 'empty' == a[0]: # empty _ queue가 비어있으면 1 출력, 아니면 0 출력
        if not q: print(1)
        else:
            print(0) 

    elif 'pop' == a[0]: # pop _ queue가 비어있으면 -1 pop, 아니면 top pop  
        if not q: print(-1)
        else:
            print(q.popleft())
