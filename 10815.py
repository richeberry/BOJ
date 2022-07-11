# n = int(input())
# cardnum = sorted(list(map(int, input().split())))
cardnum = [-10, 2, 3, 6, 10]
print(cardnum)
# m = int(input())
numlst = sorted(list(map(int, input().split())), reverse = True)
print(numlst)

ans = []
while numlst:
    if numlst.pop(0) in cardnum:
        ans.append(1)
    else:
        ans.append(0)
    print(numlst)

# for i in ans:
#     print(i, end = ' ')