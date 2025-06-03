import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

TB = N * M
blocks = [0] * 257
min_time = float('inf')
height = 0

for _ in range(N):
    row = list(map(int, input().split()))
    for height in row:
        blocks[height] += 1

for h in range(257):
    removed = 0
    need = 0
    time = 0

    for x in range(257):
        count = blocks[x]  # 높이 x 블록이 count개 있다고 가정

        if x > h:
            diff = x - h
            removed += diff * count
            time += diff * 2 * count
        elif x < h:
            diff = h - x
            need += diff * count
            time += diff * 1 * count
        # x == h 이면 아무것도 할 필요 없음

    # 인벤토리 체크: 제거된 블록 + B로 부족한 블록을 채울 수 있는지
    if removed + B < need:
        continue  # 이 h는 불가능

    if time < min_time:
        min_time = time
        height = h
    elif time == min_time:
        height = h
print(min_time, height)