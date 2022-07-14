# BOJ _ 3009

lst = [[] for _ in range(2)]
for i in range(3):
    a, b = map(int, input().split())
    lst[0].append(a)
    lst[1].append(b)


for i in range(3):

    if lst[0].count(lst[0][i]) == 1:
        a = lst[0][i]
    elif lst[1].count(lst[1][i]) == 1:
        b = lst[1][i]
print(a, b)