# 2447 _ 별 찍기 -10

n = int(input())
def star(n):
    if n== 1: return ['*']
    stars = star(n//3)
    lst = []
    for s in stars: lst.append(s*3)
    for s in stars: lst.append(s+ ' '*(n//3)+s)
    for s in stars: lst.append(s*3)
    return lst

print('\n'.join(star(n)))