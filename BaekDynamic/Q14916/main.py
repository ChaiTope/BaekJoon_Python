N = int(input())

if N == 1 or N == 3:
    print(-1)
else:
    if N % 5 == 0:
        print(N // 5)
    elif N % 5 == 1:
        print(N // 5 + 2)
    elif N % 5 == 2:
        print(N // 5 + 1)
    elif N % 5 == 3:
        print(N // 5 + 3)
    elif N % 5 == 4:
        print(N // 5 + 2)