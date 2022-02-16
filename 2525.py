# 2525 _ 오븐 시계

a,b = map(int, input().split())
c = int(input())

m = b+c 
while m > 59: # 더한 분이 59분을 초과하면
    a += 1 # 60분 받음
    m -= 60 # 60분 올림
if a > 23: # 시간이 23시를 초과하면
    a -= 24 # 00시로 바뀜
print(a,m)