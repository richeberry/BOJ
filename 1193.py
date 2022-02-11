# 1193 _ 분수찾기

n = int(input())
i = 0
while True:
	i += 1
	n -= i
	if n <= 0:
		n += i
		i += 1
		break
if i%2==0:
	print((i-n), '/', n, sep='')
else:
	print(n, '/', (i-n), sep='')