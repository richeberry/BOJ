
# BOJ _ 1463 1로 만들기

n = 5

dp = [0] * (n + 1)
dp[1] = 1

# bottom up으로 진행

# 시작 전 DP 확인
print(dp)

tmp = 1
before = dp[0]
while True:
    # 탈출 조건
    print(dp)
    print('tmp',tmp)
    print('before',before)
    if before == n:
        break

    elif (tmp * 2) % n == 0:
        dp[n] = before + 1
        before = tmp * 2
    elif (tmp * 3) % n == 0:
        dp[n] = before + 1
        before = tmp * 3
    else:
        dp[n] = before + 1
        before = tmp + 1
    tmp += 1
