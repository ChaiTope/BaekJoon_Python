import sys
input = sys.stdin.readline

N, A, B, C, D, E, F, G, H = map(int, input().split())

cnt = 0
ans = None

for x in range(N + 1):
    ax = A * x
    ex = E * x

    for y in range(N - x + 1):
        z = N - x - y

        # 첫 번째 식 체크
        if ax + B * y + C * z != D:
            continue

        # 두 번째 식 체크
        if ex + F * y + G * z != H:
            continue

        cnt += 1
        if cnt == 1:
            ans = (x, y, z)
        else:
            print(1)
            sys.exit(0)

if cnt == 0:
    print(2)
else:
    print(0)
    print(*ans)