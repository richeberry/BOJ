# 10250 _ ACM호텔

for _ in range(int(input())):
    h,w,n = map(int, input().split()) 
    floor = n%h # n번째 손님은 n-1번째 까지 채우고 난 층이므로 나머지
    room = (n//h)+1 # n-1 번째까지 채운 라인 다음 라인
    if floor == 0: # 나머지가 0이면 제일 꼭대기 층이므로 
        floor = h # 꼭대기 층
        room -= 1 # 다음 라인으로 안가므로 꽉 채운 라인 층
    print(floor * 100 + room)