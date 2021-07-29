# 8958 _ OX퀴즈

t = int(input())
x = [str(input()) for _ in range(t)]

for a in x:
    a = a.split('X')
    print(sum([int(((len(i))*(len(i)+1)/2)) for i in a]))