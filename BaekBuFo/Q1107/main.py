import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

if N == 100:
    print(0)
    sys.exit(0)

if M == 0:
    print(min(abs(N - 100), len(str(N))))
    sys.exit(0)

broken = set(list(map(int, input().split())))

ans = abs(N - 100)

for i in range(1000001):
    # i를 숫자 버튼으로 "직접 입력"할 수 있는지 검사
    ok = True

    if i == 0:
        if 0 in broken:
            ok = False
    else:
        i_copy = i
        while i_copy > 0:
            if (i_copy % 10) in broken:
                ok = False
                break
            i_copy //= 10

    if ok:
        ans = min(ans, len(str(i)) + abs(N - i))

print(ans)