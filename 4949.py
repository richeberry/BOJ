# BOJ _ 균형잡힌 세상
import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    stack = []
    flag = True

    if s == ".": # 문장이 단순히 .이면 종료
        break

    for i in s: 
        if i == '(' or i == '[': # 열린 괄호가 나오면 
            stack.append(i) # 스택에 저장
        
        elif i == ')': # 닫힌 괄호가 나오면 
            if stack and stack[-1] == '(': # 스택에 괄호가 있고, top이 ( 이라면 괄호가 완성되므로
                stack.pop() # 스택에서 ( 제거
            else: # 스택이 비었거나, top과 함께 괄호가 완성되지 않는다면
                flag = False # No
                break
            
        elif i == ']': 
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
            
    if flag and not(stack): # flag가 True이고, 스택에 아무것도 없으면 (괄호들이 완성되어서 다 제거되었으면)
        print('yes')
    else: # 아닐 경우 (flag=False or len(stack) >0)
        print('no')


