2739.

n = int(input())

for i in range(1,10):
    print(n, '*', i, '=', n*i)



10950.


t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    print(a+b)


8393.


n = int(input())
def sum_num(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    return s
print(sum_num(n))

15552.

t = int(sys.stdin.readline())
for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    i = a + b
    print(i)



2741.


import sys
n = int(sys.stdin.readline())
for i in range(1, n+1):
    print(i)

2742.

n = int(input())
for i in range(n, 0, -1):
    print(i)



뒤에 -1을 붙이면 역순으로 출력


11021.

t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')


F-string 문자열 작성 방법 익히기!
f를 접두사로 붙여 사용하고, 따옴표 안에 {}괄호를 입력하고 {}안에 변수를 넣으면 그때 그때 변수 값 출력.



11022.

t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')

F-string 진짜 편한
‘’ 안에 또 ‘’ 표시 하고 할 필요 없이 변수만 {} 처리해주면 된다는 것!


2438.(210414)


n = int(input())
for i in range(1, n+1):
    print('*' * i)

2439.


n = int(input())
for i in range(1, n+1):
    print(' ' * (n-i) + i * ‘*')

오른쪽 정렬이면 공백이 처음부터는 n-1개일 테고 하나 씩 공백이 줄어들 테니까


10871.

n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] < x:
        print(a[i], end=' ')


