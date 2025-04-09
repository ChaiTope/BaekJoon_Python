import sys

board = [list(map(int, input().split())) for _ in range(9)]

rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]
empty = []

# ⚠️ 이 부분 빠지면 안 됨!!
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num == 0:
            empty.append((i, j))
        else:
            rows[i].add(num)
            cols[j].add(num)
            boxes[(i // 3) * 3 + (j // 3)].add(num)

def solve(idx):
    if idx == len(empty):
        for row in board:
            print(' '.join(map(str, row)))
        sys.exit(0)  # 첫 번째 해만 출력하고 종료

    i, j = empty[idx]
    box_idx = (i // 3) * 3 + (j // 3)

    for num in set(range(1, 10)) - rows[i] - cols[j] - boxes[box_idx]:
        board[i][j] = num
        rows[i].add(num)
        cols[j].add(num)
        boxes[box_idx].add(num)

        solve(idx + 1)

        board[i][j] = 0
        rows[i].remove(num)
        cols[j].remove(num)
        boxes[box_idx].remove(num)

solve(0)
