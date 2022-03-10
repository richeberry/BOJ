# BOJ _  수 정렬하기 3


# 1.
n = int(input())
lst = [0]*10001 # 주어지는 최대 수의 개수
for _ in range(n):
    tmp = int(input())
    lst[tmp] += 1 # 숫자가 들어오는 인덱스에 0을 1로 바꿔줌
for i in range(10001):
    if lst[i] != 0: # 인덱스의 숫자가 0이 아니라면
        for j in range(lst[i]): # 인덱스 전까지 살펴보고 출력
            print(i)



# 2. 메모리 초과
n = int(input())
lst = [int(input()) for i in range(n)]
for _ in range(n): # lst의 최솟값의 인덱스 찾은 후 출력과 동시에 pop
    print(lst.pop(lst.index(min(lst))))