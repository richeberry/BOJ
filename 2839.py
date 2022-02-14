# 2839 _ 설탕 배달 

n = int(input())

bag = 0
while n >= 0: # 설탕이 0보다 클 때까지
    if n % 5 == 0: # 설탕이 0의 배수이면
        bag +=  (n//5) # 5로 나눈 몫의 수가 가방의 수 
        print(bag)
        break
    n -= 3 # n%5 != 0 이면 n에서 3을 빼주어 n이 5의 배수가 될 때까지 진행 
    bag += 1 # 가방 수 +1
else:
    print(-1)