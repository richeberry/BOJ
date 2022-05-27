
# BOJ _ 1463 

n = int(input())

cnt = 0

dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 1
dp[3] = 1
print(dp)
while True:
    print(n)
    # 탈출 조건
    if n == 1:
        break
    # 3으로 나누어질 때
    if n % 5 == 0:
        n -= 1 
        cnt += 1
    elif n % 3 == 0:
        n //= 3
        cnt += 1
    # 2로 나누어질 때
    elif n % 2 == 0:
        n //= 2
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)





