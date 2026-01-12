import sys

input = sys.stdin.readline

N = int(input())

stack = []
ans = 0

for i in range(N):
    n = int(input())
    cnt = 1

    while stack and stack[-1][0] < n:
        ans += stack[-1][1]
        stack.pop()

    if stack and stack[-1][0] == n:
        ans += stack[-1][1]
        cnt = stack[-1][1] + 1
        stack.pop()

    if stack:
        ans += 1

    stack.append([n, cnt])

print(ans)