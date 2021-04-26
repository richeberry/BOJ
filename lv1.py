10718. 출력(210408)

강한친구 대한육군
강한친구 대한육군

print(‘강한친구 대한육군’, ‘강한친구 대한육군’, sep = ‘\n’)



10171. 출력

\    /\
 )  ( ')
(  /  )
 \(__)|

print('\    /\\')
print(" )  ( ')")
print("(  /  )")
print(" \(__)|”)



10172. 출력

|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|


print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')



1000. 출력 (210409)

첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

첫째 줄에 A+B를 출력한다.

A,B = input().split()
print(int(A)+int(B))







1001.

첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
첫째 줄에 A-B를 출력한다.

A,B = input().split()
print(int(A)-int(B))


10998.

첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
첫째 줄에 A×B를 출력한다.

A,B = input().split()
print(int(A)*int(B))


1008.

첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
첫째 줄에 A/B를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.

A,B = input().split()
print(int(A)/int(B))

10869.
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.


1)
A,B = input().split()
x = int(A)
y = int(B)
print(x+y, x-y, x*y, x//y, x%y, sep=‘\n')

2)
Map function 사용하면

A,B = map(int, input().split())
print(A+B, A-B, A*b, A//B, A%B, sep=‘\n’)













10430.

(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

A, B, C = map(int, input().split())
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')



2588.
A = int(input())
B = input()
print(A * int(B[2]), A * int(B[1]), A * int(B[0]), A * int(B), sep='\n')



단계 1. 입출력과 사칙연산 완료!