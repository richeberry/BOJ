# 5622 _ 다이얼

dial_dict = {0:'',1:'',2:['A','B','C'],3:['D','E','F'],4:['G','H','I'], 5:['J','K','L'], 6:['M','N','O'], 
        7:['P','Q','R','S'], 8:['T','U','V'], 9:['W','X','Y','Z']} # 딕셔너리 만들어줌 이거 만드는 게 젤 귀찮았음 ^_^

s = input()
answer = 0
for i in s: # string에 있는 문자랑
    for key, value in dial_dict.items(): # 딕셔너리 item들이랑 비교해서 
        if i in value: # string 문자가 value에 있으면 key 출력
            answer += (key+1) # 1이 2초 걸리므로 1:2초 부터 시작해서 1씩 더해주면 걸리는 시간
print(answer)