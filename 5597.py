# 5597 과제 안 내신 분..?

lst = [i for i in range(1, 31)] # 1번부터 30번까지 학생

students = []

for i in range(0, 28): # 숙제 낸 학생 번호 입력받기
    students.append(int(input()))

nothomework = [x for x in lst if x not in students] # 학생이면서 숙제 내지 않은 학생 리스트 

for i in nothomework: # 한 줄에 하나씩 출력
    print(i)