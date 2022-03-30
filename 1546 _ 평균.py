# 1546
n = int(input())
a = list(map(int, input().split()))
m = max(a)
temp = 0
answer = 0
for idx, i in enumerate(a):
    temp += (i/m)
    b = (temp/len(a))*100
print(answer)