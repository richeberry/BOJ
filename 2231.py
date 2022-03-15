# BOJ _ 2231 분해합(브루트포스)

n = int(input())
for i in range(1,n):
    numlst = list(map(int, str(i))) # 한 자리에는 들어올 수 있는 수가 0부터 9이기 때문에, 10이면 [1,0] 자리수 두개로 넘어가게끔
    ans = i + sum(numlst) # 생성자와 자리수의 합 
    if ans == n: # 생성자와 자리수의 합이 분해합과 같으면
        print(i) # 생성자 출력
        break
else: # 생성자가 없으면 0 출력 
    print(0)
