# 2292 _ 벌집

num = int(input())
cnt = 1
while num > 1:
    num -= (6*cnt)
    cnt += 1
print(cnt)

# for 문 풀이

num = int(input())

for i in range(1,num+1):
    a = (6*i)-5
    b = a + b
    if num == 2:
        print(num)
        break
    if num <= b:
        print(i)
        break
