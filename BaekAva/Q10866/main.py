import sys
from collections import deque

input = sys.stdin.readline
dq = deque()
out = []

def pop_front():
    out.append(str(dq.popleft() if dq else -1))

def pop_back():
    out.append(str(dq.pop() if dq else -1))

def front():
    out.append(str(dq[0] if dq else -1))

def back():
    out.append(str(dq[-1] if dq else -1))

N = int(input())
for _ in range(N):
    cmd = input().split()

    c0 = cmd[0][0]
    if c0 == 'p':   # push / pop
        if cmd[0][1] == 'u':    # push_...
            x = cmd[1]
            if cmd[0][-1] == 't':   # push_front
                dq.appendleft(x)
            else:   # push_back
                dq.append(x)
        else:  # pop_...
            if cmd[0][-1] == 't':   # pop_front
                pop_front()
            else:   # pop_back
                pop_back()

    elif c0 == 's':
        out.append(str(len(dq)))
    elif c0 == 'e':
        out.append('1' if not dq else '0')
    elif c0 == 'f':
        front()
    else:   # 'b'
        back()

sys.stdout.write("\n".join(out))
