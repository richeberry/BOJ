# 10872 _ N!

def facto(N):
    N = int(input())
    if N == 1:
        return N
    elif N < 1:
        return 1
    else:
        return N * facto(N-1)

print(facto(N))