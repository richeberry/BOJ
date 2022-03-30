# BOJ _ 요세푸스 문제 0

# 1. 큐 사용 - 시간: 92ms
import sys
input = sys.stdin.readline
from collections import deque

N,K = map(int, input().split())
yose = deque() # 큐 설정
for i in range(1,N+1):
    yose.append(i) # 큐에 값 넣어줌
answer = []

while yose:
    yose.rotate(-(K-1)) # 왼쪽으로 K-1번 돌게 해서 yose[K-1]의 원소가 첫번째로 오게 함
    answer.append(str(yose.popleft())) # join을 위해 문자열로 추가
    

print(f'<{", ".join(answer)}>')



# 2. 큐 사용하지 않음 - 시간: 72ms
import sys
input = sys.stdin.readline
N,K = map(int, input().split())
yose = [i for i in range(1,N+1)]
answer = []
person = 0

for i in range(N):
    person += K-1 # 제거할 사람의 인덱스
    if person >= len(yose): # 사람의 인덱스가 사람 수를 넘으면 
        person = person%len(yose) # 다시 처음부터의 순서대로 
    answer.append(str(yose.pop(person))) # <> 씌워주기 위해 str로 리스트에 더하기


print(f"<{', '.join(answer)}>")



