n = int(input())
cardlst = list(map(int, input().split()))
m = int(input())
tellcard = list(map(int, input().split()))
printlst = []
for i in tellcard:
    if i in cardlst:
        printlst.append(1)
    else:
        printlst.append(0)

for i in printlst:
    print(i, end=' ')

    