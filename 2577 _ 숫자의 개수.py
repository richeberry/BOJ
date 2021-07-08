a,b,c = [int(input()) for _ in range(3)]
print(a)
tmp = a*b*c

for i in range(0,10):
    print(tmp.find(i))