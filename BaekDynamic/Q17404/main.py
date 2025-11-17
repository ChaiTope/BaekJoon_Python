import sys
input = sys.stdin.readline

INF = 10**9

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

answer = INF

# 첫 집의 색을 0(R), 1(G), 2(B)로 고정해서 3번 돌린다
for first_color in range(3):
    # prev 초기화: 첫 집만 first_color, 나머지는 불가능(INF)
    prev = [INF, INF, INF]
    prev[first_color] = cost[0][first_color]

    # 2번 집부터 N번 집까지 DP 진행
    for i in range(1, N):
        curr = [0] * 3
        curr[0] = cost[i][0] + min(prev[1], prev[2])
        curr[1] = cost[i][1] + min(prev[0], prev[2])
        curr[2] = cost[i][2] + min(prev[0], prev[1])
        prev = curr

    # 마지막 집 색은 first_color와 달라야 함
    for last_color in range(3):
        if last_color == first_color:
            continue
        answer = min(answer, prev[last_color])

print(answer)
