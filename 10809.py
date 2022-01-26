
s = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    if i in s:
        print(s.index(i), end=' ') # idx 는 안됨 / 줄 바꾸기가 아니고 띄어쓰기로 출력
    else:
        print(-1, end=' ') 
