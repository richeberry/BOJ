# BOJ _ 오큰수

# 1.


n = int(input())
lst = list(map(int, input().split()))
cnt = [0] # 0으로 숫자 비교 시작 -> 오큰수 
ans = [-1] * n # 따로 -1 더해주지않고 처음부터 -1 리스트로 만들어줌 => 연산 줄일 수 있음
for i in range(1,n):
    while cnt and lst[cnt[-1]] < lst[i]: # 오른쪽 값이 왼쪽값보다 크면 오큰수이므로
        ans[cnt.pop()] = lst[i] # cnt 인덱스 제거와 동시에 ans 리스트에 값 저장
    
    cnt.append(i) # cnt 인덱스 1 더해줌
    print('cnt',cnt)

print(*ans)



# 2. 시간초과....

# import sys
# input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

ans = []
for i in range(len(n)):
    tmp = lst[i] # 처음 입력받은 값으로 비교 시작
    stack = sorted(lst[i+1:]) # 처음 값을 제외한 나머지 값들을 스택에 넣어줌
    print(tmp, stack)
    while stack: 
        if stack[0] > tmp: # 스택값이 비교값보다 크면 오큰수이므로
            ans.append(stack[0]) # ans에 값 저장
            break
        else: # 스택값이 비교값보다 작으면 오큰수가 아니므로
            stack.pop(0) # 스택의 처음 값 제거 -> 큰 수가 나올 떄까지 루프를 돌며 pop
    if not stack: # 스택이 비어있으면 큰 값이 없는 것이므로
        ans.append(-1) # -1 출력

for i in ans:
    print(i, end=' ')