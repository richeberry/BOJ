# 2908 _ 상수

# 최종 풀이
a,b = list(map(str, input().split()))

a = a[::-1] # ::-1 : 역순 -> string만 가능하고 list, int 안됨
b = b[::-1]
print(max(a,b))



# 첫번째 풀이 (틀림)
import sys
input = sys.stdin.readline

a,b = input().split()
# 상수가 숫자로 거꾸로 읽음
# 두 수는 같지 않은 세 자리 수 

ans = []
def back(num):
    if len(ans) >= 3: return int(''.join(map(str, ans)))
    ans.append(num%10)
    return back(num//10)

print(max(back(a),back(b)))




