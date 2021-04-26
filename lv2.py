1330.


A,B = map(int, input().split())
if A > B:
  print('>')
elif A < B:
  print('<')
else:
  print(‘==')



9498.

X = int(input())
if 100 >= X >= 90:
  print('A')
elif 89 >= X >= 80:
  print('B')
elif 79 >= X >= 70:
  print('C')
elif 69 >= X >= 60:
  print('D')
else:
  print(‘F')



2753.

A = int(input())
if A % 4 == 0 and A % 100 != 0 or A % 400 == 0:
  print('1')
else:
  print(‘0')


14681. (210412)


x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
else:
    print("4")


2884.

H, M = map(int, input().split())
M = M - 45
if H <= 0 and M < 0:
    H= H+24
    H = H-1
    M = M+60
elif M >= 60:
     H = H+1
     M = M-60
elif M < 0:
    H = H-1
    M = M+60

print(H,M)
(맞았긴 한데 너무 답이 구차해서………… 다시 해보겠음)

2)
H,M = map(int, input().split())
M -= 45
if M < 45:
    if H == 0:
        H = 23
        M += 60
    else:
        H -= 1
        M += 60

print(H, M)



