# 2750 정렬

t = int(input())
lst = []
for i in range(t):
    i = list(map(int, input().split()))
    lst += i
for num in sorted(lst):
    print(num)