N = int(input())

if N == 1:
    print(0, 1)
elif N == 2:
    print(1, 0)
else:
    A = 1
    B = 1
    result = 0
    for i in range(2, N):
        result = A + B
        B = result
        A = result - A
    print(A, B)