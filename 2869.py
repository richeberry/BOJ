# 2869 _ 달팽이는 올라가고 싶다

import math
import sys
# input = sys.stdin.readline

a,b,v = map(int, input().split()) 

day  = math.ceil((v-b)/(a-b))
        
print(day)

# v = day(a-b)
# day = v / (a-b)
# 정상에 만약 도착했으면, 다시 미끄러지지 않으므로 
# v = v-b (이미 미끄러진 높이로 계산)