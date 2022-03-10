# 하노이 탑 이동 순서
# 무조건 첫 번째 장대에서 세 번째 장대로 원판 이동
# 한 번에 한 개의 원판만 이동
# 항상 위의 것이 아래의 것보다 작아야 함
n = 3
a = [i for i in range(1,n+1)]
b = []
c = []

# 두 개를 비교했을 때 pop, stack 
def hanoi(n, lst1, lst2, lst3, cnt=0):
    if lst2[0] > lst1[0]:
        lst2.append(lst1.pop(0))
    else:
        hanoi(lst1, lst3)

    return hanoi(n)


print(hanoi(n,a,b,c))

# for i in a:
#     print(i)