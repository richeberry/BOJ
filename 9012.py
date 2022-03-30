# BOJ silver.4 _ 9012 (괄호)


for _ in range(int(input())):
    stack = []
    stop = 0
    ps = input()
    for s in ps: # 문자열 하나씩 뜯어보기
        if s == '(': # '(' 이면 stack list에 추가
            stack.append(1)
        if s == ')': # ')' 일 때 
            if len(stack) > 0: # stack에 원소가 있으면
                stack.pop() # 원소 pop
            else: # stack에 원소가 없으면
                print('NO') # 'NO' 출력 후 
                stop += 1 # 비어있는 stack에서 pop 시도했으면 -> 남은 (가 없는데 )가 먼저 나왔으면 + 1
                break # 탈출
    if len(stack) == 0: # stack list가 비어있고
        if stop == 0: # 비어있는 stack에서 pop 시도하지 않았으면
            print('YES') 
    else: # stack 원소가 남아있으면
        print('NO')
