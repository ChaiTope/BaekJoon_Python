import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().rstrip())) for _ in range(9)]

# 1) 빈 칸 좌표 모아두기
empties = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            empties.append((i, j))

# 2) row_used, col_used, blk_used 초기화
# blk 인덱스: (i//3)*3 + (j//3)  → 0~8번 블록
row_used = [[False]*10 for _ in range(9)]
col_used = [[False]*10 for _ in range(9)]
blk_used = [[False]*10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        num = sudoku[i][j]
        if num != 0:
            row_used[i][num] = True
            col_used[j][num] = True
            b = (i//3)*3 + (j//3)
            blk_used[b][num] = True

# 3) 백트래킹 함수
def dfs(idx):
    # 기저조건: 빈 칸을 전부 채웠으면 출력 후 종료
    if idx == len(empties):
        for row in sudoku:
            print("".join(map(str, row)))
        sys.exit(0)

    x, y = empties[idx]
    b = (x//3)*3 + (y//3)

    # 1~9까지 시도
    for num in range(1, 10):
        if not row_used[x][num] and not col_used[y][num] and not blk_used[b][num]:
            # num을 놓을 수 있으면
            sudoku[x][y] = num
            row_used[x][num] = True
            col_used[y][num] = True
            blk_used[b][num] = True

            dfs(idx + 1)

            # 되돌리기
            sudoku[x][y] = 0
            row_used[x][num] = False
            col_used[y][num] = False
            blk_used[b][num] = False

    # 여기까지 왔다는 건 1~9 중 어디에도 넣을 수 없어서 이전 호출부로 백트랙 해야 한다는 뜻
    return

# 4) DFS 시작
dfs(0)