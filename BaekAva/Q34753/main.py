import heapq
import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
# 줄 개수
L = 2*N + 2

rem = [0] * L      # 각 줄의 남은 시간 합
done = [False] * L
solved = bytearray(N*N)

# 행
for i in range(N):
    rem[i] = sum(board[i])

# 열
for j in range(N):
    s = 0
    for i in range(N):
        s += board[i][j]
    rem[N + j] = s

# 대각
rem[2*N] = sum(board[i][i] for i in range(N))
rem[2*N+1] = sum(board[i][N-1-i] for i in range(N))

pq = []

for i in range(N):
    heapq.heappush(pq,(rem[i], 0, i, i))
for j in range(N):
    heapq.heappush(pq, (rem[N+j], 1, j, N+j))
heapq.heappush(pq, (rem[2 * N], 2, 0, 2 * N))
heapq.heappush(pq, (rem[2*N+1], 3, 0, 2*N+1))

ans = [0] * (L + 1)   # 1..L 사용
T = 0
b = 0
filled_k = 0

def push_line(line_id):
    """현재 rem[line_id] 값을 기준으로 힙에 (최신 후보) 하나 넣기"""
    if done[line_id]:
        return
    if line_id < N:
        heapq.heappush(pq, (rem[line_id], 0, line_id, line_id))          # (sum, type, num, id)
    elif line_id < 2 * N:
        j = line_id - N
        heapq.heappush(pq, (rem[line_id], 1, j, line_id))
    elif line_id == 2 * N:
        heapq.heappush(pq, (rem[line_id], 2, 0, line_id))
    else:  # 2N+1
        heapq.heappush(pq, (rem[line_id], 3, 0, line_id))

def pick_line():
    """힙에서 유효한(최신 rem, 아직 미완성) 줄 하나를 뽑아 반환"""
    while True:
        cur_rem, typ, num, line_id = heapq.heappop(pq)
        if done[line_id]:
            continue
        if cur_rem != rem[line_id]:
            continue  # 구버전
        return line_id

# 최대 L번(줄 개수만큼)만 선택하면 끝
while filled_k < L:
    line = pick_line()

    changed = set()

    # ---- (1) 선택된 줄의 남은 칸들을 실제로 풀기 ----
    if line < N:
        # 행 r
        r = line
        for j in range(N):
            idx = r * N + j
            if solved[idx]:
                continue
            solved[idx] = 1
            a = board[r][j]
            T += a

            # rem 감소
            rem[r] -= a
            rem[N + j] -= a
            changed.add(r)
            changed.add(N + j)

            if r == j:
                rem[2 * N] -= a
                changed.add(2 * N)
            if r + j == N - 1:
                rem[2 * N + 1] -= a
                changed.add(2 * N + 1)

    elif line < 2 * N:
        # 열 c
        c = line - N
        for i in range(N):
            idx = i * N + c
            if solved[idx]:
                continue
            solved[idx] = 1
            a = board[i][c]
            T += a

            rem[i] -= a
            rem[N + c] -= a
            changed.add(i)
            changed.add(N + c)

            if i == c:
                rem[2 * N] -= a
                changed.add(2 * N)
            if i + c == N - 1:
                rem[2 * N + 1] -= a
                changed.add(2 * N + 1)

    elif line == 2 * N:
        # ↘ 대각
        for i in range(N):
            j = i
            idx = i * N + j
            if solved[idx]:
                continue
            solved[idx] = 1
            a = board[i][j]
            T += a

            rem[i] -= a
            rem[N + j] -= a
            rem[2 * N] -= a
            changed.add(i)
            changed.add(N + j)
            changed.add(2 * N)

            if i + j == N - 1:
                rem[2 * N + 1] -= a
                changed.add(2 * N + 1)

    else:
        # ↙ 대각
        for i in range(N):
            j = N - 1 - i
            idx = i * N + j
            if solved[idx]:
                continue
            solved[idx] = 1
            a = board[i][j]
            T += a

            rem[i] -= a
            rem[N + j] -= a
            rem[2 * N + 1] -= a
            changed.add(i)
            changed.add(N + j)
            changed.add(2 * N + 1)

            if i == j:
                rem[2 * N] -= a
                changed.add(2 * N)

    # ---- (2) 선택된 줄 완료 처리 ----
    if not done[line]:
        done[line] = True
        b += 1

    # ---- (3) 자동 완성(rem==0) 줄 처리 ----
    # (이건 턴마다 L(≈3000) 훑어도 OK)
    for x in range(L):
        if (not done[x]) and rem[x] == 0:
            done[x] = True
            b += 1

    # ---- (4) 정답 채우기: 처음으로 k빙고 이상이 된 시간 ----
    while filled_k < b:
        filled_k += 1
        ans[filled_k] = T

    # ---- (5) 이번 턴에서 rem이 바뀐 줄들을 힙에 "최신값"으로 다시 넣기 ----
    for x in changed:
        push_line(x)

# 출력
for k in range(1, L + 1):
    print(ans[k])