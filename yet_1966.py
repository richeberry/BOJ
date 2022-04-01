# BOJ _ 1966 프린터 큐 

# where = 0
# case = [1,1,9,1,1,1]
# case = [1,2,3,4]
# case = [5]


for i in range(int(input())):
    N,M = map(int, input().split())
    case = list(map(int, input().split()))
    num = case[M]
    print(num)
    cnt = 0
    while case:
        if case.index(max(case)) != num:
            print(case)
            case.append(case.pop(0))
            print(case)
        elif case[0] == num:
            case.pop(0)
            cnt += 1
            break
        

    print(cnt)