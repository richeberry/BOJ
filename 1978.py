# 1978 _ 소수 찾기

n = int(input())
number = map(int, input().split())
prime = 0
for num in number:
    ans = 0 # ans 약수 초기화
    if num > 1: # 소수: 1과 자기의 자신만을 약수로 갖는 수 
        for j in range(2,num):  # 2부터 num-1까지 하나씩 나누어 떨어지는지 보기
            if num % j == 0: # 약수이면
                ans += 1 
        if ans == 0: # 나누어 떨어지는 수가 없으면
            prime += 1 # 소수

print(prime)