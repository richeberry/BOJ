# BOJ _ 7568 _ 덩치

n = int(input())
data = [] # 정보를 담을 리스트 초기화
ans = [] # 등수를 담을 리스트 초기화

for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b)) # tuple 형태로 리스트에 저장

for i in range(n):
    cnt = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:  # 몸무게와 키 전부 다 현재 데이터보다 이상이면
            cnt += 1 # 등수 + 1
    ans.append(cnt + 1) # 현재 등수 리스트에 추가

print(ans)




