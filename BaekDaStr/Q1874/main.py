import sys

input = sys.stdin.readline

n = int(input())
target = [int(input()) for _ in range(n)]
stack = []
current = 1
ops = []

for x in target:
    # x가 나올 때까지 push
    while current <= x:
        stack.append(current)
        ops.append('+')
        current += 1

    # top이 x면 pop
    if stack[-1] == x:
        stack.pop()
        ops.append('-')
    else:
        print("NO")
        sys.exit()

# 여기에 도달했으면 성공
print('\n'.join(ops))