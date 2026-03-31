import sys

input = sys.stdin.readline

N = sorted(list(map(int, input().rstrip())), reverse=True)

if 0 not in N:
    print(-1)
    sys.exit(0)

if sum(N) % 3 == 0:
    print(*N, sep="")
else:
    print(-1)