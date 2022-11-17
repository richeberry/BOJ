
# BOJ _ 1463 1로 만들기

x = int(input())

dp = [0] * (x + 1)

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1 # 2와 3으로 나누어지지 않는 숫자면 -1을 해야하기 때문에 1씩 증가시켜줌

    if i % 2 == 0: # 2로 나누어지면
        dp[i] = min(dp[i], dp[i//2] + 1) # dp에 저장된 수와 i를 2로 나누었을 때의 숫자와 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1) # dp에 저장된 수와 i를 3으로 나누었을 떄의 숫자와 비교

print(dp[x])
