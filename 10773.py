# BOJ _ 제로 (스택)


stack = [] # number list 
for num in range(int(input())):
    n = int(input())
    if n == 0: # if n == 0
        stack.pop(-1) # delete recent number
    else: # or
        stack.append(n) # add

print(sum(stack))