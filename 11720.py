'''
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

'''
# 다른 풀이
n = input()
print(sum(map(int,input())))

# 내 풀이
a,b = input().split()
b = list(b)
print(sum([int(n) for n in b]))


    