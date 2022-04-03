# BOJ _ 1966 프린터 큐 

# where = 0
# case = [1,1,9,1,1,1]
# case = [1,2,3,4]
# case = [5]


from collections import deque
for i in range(int(input())):
    N,M = map(int, input().split())
    case = deque(list(map(int, input().split())))
    idx_case = deque(list(range(N))) # 중복 숫자가 나올 수도 있으므로 idx로 구분해주기 위함
    cnt = 0

    while case:
        if case[0] == max(case): # 중요도가 가장 높은 서류가 case의 top에 있으면
            cnt += 1 
            case.popleft() # 프린트
            if idx_case.popleft() == M: # case를 popleft 한 것처럼 idx case에서도 제거하는데, 원래 출력하려는 idx와 같으면
                print(cnt) # 여기까지만 출력하면 되므로 print(cnt)

        else:
            case.rotate(-1)
            idx_case.rotate(-1)