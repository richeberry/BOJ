# 10870 _ 피보나치 수 

num = int(input())
def fibo(num):
    if num <= 1:
        return num
    return fibo(num-1) + fibo(num-2)

print(fibo(num))