N = int(input())
if N != 0:
    M = 1
    for i in range(1, N+1):
        M *= i
    print(M)
else:
    print(1)