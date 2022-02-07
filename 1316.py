# 1316 _ 그룹 단어 체커

t = int(input())
cnt = t
for _ in range(t):
    word = input()

for i in range(len(word)-1): # word[i+1]까지 확인해야하므로 -1
    if word.find(word[i]) > (word.find(word[i+1])): 
        # find : 같은 문자열이 나와도 처음 그 문자열이 나온 인덱스를 출력
        # 앞의 인덱스 번호보다 뒤의 인덱스 번호가 더 크면 -> 앞에 나왔던 문자열이 뒤에 또 나온 것이 되므로 그룹 문자가 아님
        cnt -= 1
        break # 하나만 나와도 그룹 단어 아니므로
print(cnt)