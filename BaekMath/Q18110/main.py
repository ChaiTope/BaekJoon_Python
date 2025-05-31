import sys
input = sys.stdin.readline

N = int(input())
if N == 0:
    print(0)
else:
    level = [int(input()) for _ in range(N)]
    level.sort()

    t = int(N * 0.15 + 0.5)
    low = t
    high = N - t

    cut_array = level[low:high]

    total = sum(cut_array)
    L = len(cut_array)
    avg = total / L

    answer = int(avg + 0.5)
    print(answer)
