# BOJ _ 피보나치 함수
# 메모이제이션

n = int(input())
dp = [0] * 41
dp[1] = 1
dp[2] = 1

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
print(dp[2],dp[1])