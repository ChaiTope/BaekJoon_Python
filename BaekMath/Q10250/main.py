T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    count = 0
    while N > 0:
        N -= H
        count += 1
    N += H
    print(N * 100 + count)