import sys
input = sys.stdin.readline

S = set()
N = int(input())
for _ in range(N):
    cmd = input().split()
    op = cmd[0]
    if op == 'add':
        S.add(int(cmd[1]))
    elif op == 'remove':
        S.discard(int(cmd[1]))
    elif op == 'check':
        print(1 if int(cmd[1]) in S else 0)
    elif op == 'toggle':
        x = int(cmd[1])
        if x in S: S.remove(x)
        else:      S.add(x)
    elif op == 'empty':
        S.clear()
    elif op == 'all':
        S = set(range(1,21))
