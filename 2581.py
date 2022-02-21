# 2581 _ 소수


m = int(input())
n = int(input())
primelst = []
for num in range(m,n+1): # 나눠지는 숫자
    ans = 0
    if num > 1: # 소수: 1과 자기의 자신만을 약수로 갖는 수 
        for j in range(2,num): # num을 차례로 나눌 숫자
            if num % j == 0: # 나누어 떨어지면
                ans += 1 # ans에 1 추가
                break
        if ans == 0: # 나누어 떨어지는 수가 없으면 
            primelst.append(num) # 소수리스트에 추가
if len(primelst) == 0:
    print(-1)
else:
    print(sum(primelst),primelst[0],sep='\n') # 소수리스트 합과 제일 작은 값 출력