# BOJ _ 피보나치 함수
# 메모이제이션

# 피보나치 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

t = int(input())

def fibonacci(n):
    dp = [0] * (n + 3)
    dp[0] = [1,0]
    dp[1] = [0,1]

    if n > 1:
        for i in range(2, n + 1):
            dp[i] = [x + y for x, y in zip(dp[i-1],dp[i-2])]
    return dp[i]

for _ in range(t):
    n = int(input())
    ans = fibonacci(n)
    for i in ans:
        print(i, end=' ')

