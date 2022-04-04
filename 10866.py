# BOJ _ 10866 덱

from collections import deque
import sys
input = sys.stdin.readline

numlst = deque()
for i in range(int(input())):
    order = list(map(str, input().split()))
    o0 = order[0]
    if len(order) > 1:
        o1 = order[1]

        if o0 == 'push_back':
            numlst.append(o1)
        elif o0 == 'push_front':
            numlst.appendleft(o1)
            
    elif o0 == 'size':
        print(len(numlst))
    elif o0 == 'empty':
        if not numlst:
            print(1)
        else: print(0)
        
    else:
        if numlst:
            if o0 == 'front':
                print(numlst[0])
            elif o0 == 'back':
                print(numlst[-1])
            if o0 == 'pop_front':
                print(numlst.popleft())
            elif o0 == 'pop_back':
                print(numlst.pop())
        else:
            print(-1)

