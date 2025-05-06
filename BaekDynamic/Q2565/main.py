import sys
input = sys.stdin.readline

n = int(input())                 # 전깃줄 개수
wires = []                       # [(left, right), ...]

for _ in range(n):
    left, right = map(int, input().split())
    wires.append((left, right))

# 1) 왼쪽 위치 기준으로 정렬
wires.sort(key=lambda x: x[0])

# 2) 오른쪽 위치만 뽑아서 리스트로
right_positions = [r for _, r in wires]

# 3) LIS 길이 구하기
dp = [1] * n                     # dp[i]: i번째까지의 오른쪽 위치로 끝나는 LIS 길이
for i in range(n):
    for j in range(i):
        if right_positions[j] < right_positions[i]:
            dp[i] = max(dp[i], dp[j] + 1)

lis_length = max(dp)

# 4) 최소 제거 횟수
print(n - lis_length)
