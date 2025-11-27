import sys
from collections import Counter

input = sys.stdin.readline

T = int(input())

subA = []
subB = []

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

answer = 0

for i in range(n):
    s = 0
    for j in range(i, n):
        s += A[j]
        subA.append(s)

for i in range(m):
    s = 0
    for j in range(i, m):
        s += B[j]
        subB.append(s)

countA = Counter(subA)
countB = Counter(subB)

for x in countA:
    answer += countA[x] * countB.get(T - x, 0)

print(answer)