import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
MAX = max(numbers)

freq = [[0, 0] for _ in range(MAX + 1)]

for i in numbers:
    freq[i][0] = 1

for i in numbers:
    for m in range(i*2, MAX + 1, i):
        if freq[m][0] == 1:
            freq[i][1] += 1
            freq[m][1] -= 1

for x in numbers:
    print(freq[x][1], end=' ')