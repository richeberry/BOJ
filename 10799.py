# BOJ _ 10799 쇠막대기


lst = list(input())
stack = []
answer = 0

for i in range(len(lst)):
    if lst[i] == '(': # '(' 가 나오면 stack에 쌓기
        stack.append(input[i])

    else: # ')'가 나오면 
        if lst[i-1] == '(': # 바로 전의 input이 '('였다면 -> 레이저이므로 
            stack.pop() # stack에서 제거
            answer += len(stack) # 지금까지의 막대기 개수 더하기
        else: # 바로 전의 input이 ')'였으면 -> 쇠막대기 끝이므로 
            stack.pop() # stack에서 제거
            answer += 1 # 막대기 끝 더하기 

print(answer)
