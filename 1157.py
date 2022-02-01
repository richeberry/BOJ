# 1157 _ 단어 공부


s = input().upper() # 문자열 대문자로 바꾸기
s_list = list(set(s)) # 중복 문자열 제거 - 같은 문자열의 개수를 반복해서 셀 필요 없음

cnt = [] # 중복 문자열 개수 리스트
for i in s_list: 
    cnt.append(s.count(i)) # 문자열 센 개수 리스트에 추가
if cnt.count(max(cnt)) > 1: # 제일 큰 중복문자열 수가 1개 초과이면 
    print('?') # ? 출력
else:
    print(s_list[cnt.index(max(cnt))])
    # 중복 문자열 리스트에서 가장 큰 수
    # 의 인덱스를 찾아옴
    # 중복 제거된 문자열에서 그 인덱스에 해당하는 문자열 출력
