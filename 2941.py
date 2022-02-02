# 2941 _ 크로아티아 알파벳

s = input()
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z='] # 크로아티아 문자 리스트
answer = 0
for i in croatia: 
    if i in s: # s에 크로아티아 문자 있으면 
        s = s.replace(i,str(1)) # 1로 치환
print(len(s)) # 문자 개수 출력
        