N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]

prev = triangle[0]        # 길이 1
for i in range(1, N):
    curr = [0]*(i+1)      # 매 줄 길이가 달라지지만 최대 N
    for j in range(i+1):
        if j == 0:
            curr[j] = prev[j] + triangle[i][j]
        elif j == i:
            curr[j] = prev[j-1] + triangle[i][j]
        else:
            curr[j] = max(prev[j-1], prev[j]) + triangle[i][j]
    prev = curr
print(max(prev))
