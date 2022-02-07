# 2675 문자열 반복

t = int(input())

for _ in range(t): # 받은 t의 수 만큼
    n,s = map(str, input().split()) # 스플릿하여 입력 받음
    for i in s: # 문자열 중 하나를 받아
        print(i*int(n), end='') # n개씩 곱하여 출력
    print()