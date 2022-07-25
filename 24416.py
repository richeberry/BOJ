# BOJ _ 24416 _ 피보나치수

n = int(input())

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

f = [0] * (n + 1)
def fibonacci(n, cnt):
    f[1] = 1
    f[2] = 1
    for i in range(3, n):
        cnt += 1
        f[i] = f[i - 1] + f[i - 2]
    return cnt

print(fib(n), fibonacci(n, 1))