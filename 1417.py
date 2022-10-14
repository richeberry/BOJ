# 국회의원 선거

n = int(input())
dasom = int(input())
candi = []
cnt = 0

for i in range(n-1):
    m = int(input())
    candi.append(m)

if n == 1:
    pass
else:
    while dasom <= max(candi): # 다솜이가 최대득표자가 될 때까지
        dasom += 1
        cnt += 1
        candi[candi.index(max(candi))] -= 1 # 최대득표에서 하나 빼기
    
print(cnt)