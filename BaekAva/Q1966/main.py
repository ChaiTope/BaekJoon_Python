import sys
from collections import deque

input = sys.stdin.readline

from collections import deque

def solve():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))  # 문서들의 우선순위 목록

    q = deque()
    for i in range(N):
        # (우선순위, 원래위치) 쌍으로 큐에 넣어 둠
        q.append((arr[i], i))

    printed = 0
    while q:
        cur_prio, cur_idx = q.popleft()
        # 뒤에 더 큰 우선순위가 있으면 뒤로 재삽입
        if any(cur_prio < other_prio for other_prio, _ in q):
            q.append((cur_prio, cur_idx))
        else:
            # 실제로 출력할 차례
            printed += 1
            if cur_idx == M:
                print(printed)
                return

for i in range(int(input())):
    solve()