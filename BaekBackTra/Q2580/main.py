board = [list(map(int, input().split())) for _ in range(9)]

rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]
empty = []

for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num == 0:
            empty.append((i, j))
        else:
            rows[i].add(num)
            cols[j].add(num)
            boxes[(i // 3) * 3 + (j // 3)].add(num)

