# BOJ _ 피보나치 함수
# 메모이제이션

# 피보나치 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

t = int(input())

# fibonacci 점화식: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
# fibonacci(0) = 1
# fibonacci(1) = 1
def fibonacci(n):
    dp = [0] * (n + 3) # 넉넉하게 리스트 길이 만듦
    dp[0] = [1,0] # 0일 때 fibonacci(0)은 한 번 호출됨
    dp[1] = [0,1] # 1일 때 fibonacci(1)은 한 번 호출됨

    if n > 1: # 마지막 범위가 2보다 작은 경우 제외하기 위해
        for i in range(2, n + 1):
            # n-1 자리의 값과 n-2 자리의 값을 각각 더해줌 
            dp[i] = [x + y for x, y in zip(dp[i-1],dp[i-2])] 
    # 최종 n자리의 값 출력
    return dp[n]

for _ in range(t):
    n = int(input())
    ans = fibonacci(n)
    for i in ans:
        print(i, end = ' ')
    print()

