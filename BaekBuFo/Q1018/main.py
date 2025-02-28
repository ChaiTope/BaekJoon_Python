N, M = map(int, input().split())  # 보드 크기 입력받기
board = [input() for _ in range(N)]  # 보드 입력

WB = [
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
]
BW = [
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
]

min_count = float('inf') # 가장 큰 값으로 초기화

# 8x8 체스판을 만들 수 있는 모든 구간 탐색
for i in range(N - 7):  # 세로 범위
        for j in range(M - 7):  # 가로 범위
                count_WB = 0  # WB 패턴과 다른 개수
                count_BW = 0  # BW 패턴과 다른 개수

                # i, j에서 시작하는 검사
                for x in range(8):
                        for y in range(8):
                                if board[i + x][j + y] != WB[x][y]:
                                        count_WB += 1
                                if board[i + x][j + y] != BW[x][y]:
                                        count_BW += 1

                # 현재 8 * 8 보드가 최소라면 갱신
                min_count = min(min_count, count_WB, count_BW)

print(min_count)