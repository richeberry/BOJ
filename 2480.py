# BOJ _ 2480

money_lst = [] # 상금 저장할 리스트 초기화

# 세 개의 주사위 던져서 같은 눈 수에 따라 게산

dice = list(map(int,input().split()))
if len(set(dice)) == 1: # 세 주사위의 눈이 다 같으면
    money_lst.append(10000 + dice[0] * 1000) 
elif len(set(dice)) == 2: # 주사위의 눈이 두 개만 같으면
    tmp = dice[0] # 같은 눈을 저장할 변수
    for j in range(1, len(dice)):
        if tmp == dice[j]: # 같은 눈이 나오면 그 눈으로 계산
            money_lst.append(1000 + tmp * 100)
else: # 같은 눈이 하나도 없으면
    money_lst.append(max(dice) * 100)

print(max(money_lst))


# 다른 풀이
a, b, c = map(int, input().split())
 
if a == b and b == c:    # 3개가 동일한 경우
    print(10000 + (a * 1000))
 
elif a == b or b == c:    # 2개가 동일한 경우
    print(1000 + (b * 100))
 
elif a == c:    # 2개가 동일한 경우
    print(1000 + (a * 100))
 
else:    # 모두 다른 경우
    print(max(a, b, c)*100)