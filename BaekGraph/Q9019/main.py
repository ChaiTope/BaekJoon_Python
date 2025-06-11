from collections import deque
import sys
input = sys.stdin.readline

# 1) 전이 테이블 미리 계산
D_table = [(i*2)%10000 for i in range(10000)]
S_table = [9999 if i==0 else i-1 for i in range(10000)]
L_table = [(i%1000)*10 + (i//1000) for i in range(10000)]
R_table = [(i%10)*1000 + (i//10) for i in range(10000)]
ops = [(D_table, 'D'), (S_table, 'S'), (L_table, 'L'), (R_table, 'R')]

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [False]*10000
    parent  = [-1]*10000
    how     = ['']*10000

    q = deque([A])
    visited[A] = True

    while q:
        cur = q.popleft()
        if cur == B:
            break
        for table, ch in ops:
            nxt = table[cur]
            if not visited[nxt]:
                visited[nxt] = True
                parent[nxt]  = cur
                how[nxt]     = ch
                q.append(nxt)

    # 결과 역추적
    res = []
    x = B
    while x != A:
        res.append(how[x])
        x = parent[x]
    print(''.join(reversed(res)))
