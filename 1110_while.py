
n = int(input())
temp = n
cnt = 0

while True:
    x = temp % 10 # 1의 자리 - 6
    y = temp // 10 # 10의 자리 - 2
    z = (x+y)%10 #다시 1의 자리 만들어주기 - 8
    temp = (x*10)+z # - 68

    cnt += 1
    if temp == n:
        break

print(cnt)