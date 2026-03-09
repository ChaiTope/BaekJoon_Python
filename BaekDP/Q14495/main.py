import sys
input = sys.stdin.readline

N = int(input())

a, b, c = 1, 1, 1
for _ in range(3, N):
    a, b, c = b, c, a + c

print(c)
