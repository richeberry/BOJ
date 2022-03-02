# BOJ _ 스택 수열


stack = []
answer = []
cnt = 0
flag = True
for _ in range(int(input())):
    num = int(input())

    while cnt < num: # 1부터 num까지 stack에 push
        cnt += 1
        stack.append(cnt)
        answer.append('+') # push할 때마다 '+' 
        

    if stack[-1] == num: # stacklist에서 top이 input num과 같으면
        stack.pop() # pop
        answer.append('-') # pop할 때마다 '-'

    else: 
        flag = False # 맞지 않으면 'NO' 출력 준비
        break

if flag == False:
    print('N0')
else:
    for i in answer: # 줄바꿈 출력
        print(i)