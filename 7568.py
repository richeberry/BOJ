# BOJ _ 7568 _ 덩치


n = 5
num = [0] * n
num[0] = 1
people = [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]

for i in range(n):
    person = people[i]
    print('person', person)
    for j in range(1, n):
        person2 = people[j]
        print('2', person2)
        if person[0] < person2[0] and person[1] < person2[1]:
            num[i] += 1
        elif person[0] > person2[0] and person[1] > person2[1]:
            num[j] += 1
        else:
            continue

    print(num)



print(num)




