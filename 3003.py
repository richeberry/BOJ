# 킹, 퀸, 룩, 비숍, 나이트, 폰

n = list(map(int, input().split()))

origin  = [1, 1, 2, 2, 2, 8]

diff = []

for i in range(len((origin))):
    print(origin[i] - n[i], end = ' ')

