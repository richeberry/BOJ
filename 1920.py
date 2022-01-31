# 1920 _ 수 찾기

import sys
input = sys.stdin.readline
n = int(input())
nlist = list(map(int, input().split(' ')))
m = int(input())
mlist = list(map(int, input().split(' ')))

nlist.sort() # 이진 분할 정의 - 정렬 되어있는 배열에서 찾는 것

def bsch(lst, num, start, end):
    while start <= end:
        mid = (start+end) // 2 # 이진 분할 
        if lst[mid] == num: # 중앙값과 같으면
            return True # True 반환 -> 이진 분할
        
        elif lst[mid] > num: # 중앙값이 더 크면
            end = mid - 1 # 끝값을 중앙값 앞으로 -> 리스트 앞으로 분할해줌 
            
        else: # 중앙값이 더 작으면
            start = mid + 1 # 시작값을 중앙값 뒤로 -> 리스트 뒤로 분할해줌
    return False

for num in mlist: # mlist에 있는 값 순서대로 비교
    if bsch(nlist, num, 0, n-1): #nlist와 비교, end = nlist 길이 -1
        print(1)
    else:
        print(0)