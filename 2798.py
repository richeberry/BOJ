# BOJ _ 2798 블랙잭

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
lst =  list(map(int, input().split()))

from itertools import combinations

perm = list(combinations(lst,3))

tmp = []
for ele in perm:
    if sum(ele) <= m:
        tmp.append(sum(ele))

print(sorted(tmp)[-1])

