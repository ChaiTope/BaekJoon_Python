n, k = map(int, input().split())

if k > n:
    print(0)
elif k < 0:
    print(0)
else:
    nsum = 1
    for i in range(1, n + 1):
        nsum *= i
    ksum = 1
    for i in range(1, k + 1):
        ksum *= i

    nksum = 1
    for i in range(1, n-k+1):
        nksum *= i

    print(nsum//(ksum*nksum))