# 2675 문자열 반복

t = int(input())

for _ in range(t):
    n,s = map(str, input().split())
    for i in s:
        print(i*int(n), end='')
    print()