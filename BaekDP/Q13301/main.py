N = int(input())

if N == 1:
    print(4)
elif N == 2:
    print(6)
else:
    A, B = 1, 1
    result = 0
    for i in range(2, N):
        result = A + B
        B = result
        A = result - A
    print(2*A + 4*B)