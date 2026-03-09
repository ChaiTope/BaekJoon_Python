import sys
input = sys.stdin.readline

H, W = map(int, input().split())
walls = list(map(int, input().split()))

stack = []    # 인덱스 저장
ans = 0

for i in range(W):
    # 현재 벽이 더 높아져서 "골"이 닫히는 동안 반복
    while stack and walls[i] > walls[stack[-1]]:
        bottom = stack.pop()    # 골 바닥

        if not stack:
            break  # 왼쪽 벽이 없으면 물 못 고임

        left = stack[-1]    # 왼쪽 벽 인덱스
        right = i   # 오른쪽 벽 인덱스(현재)

        height = min(walls[left], walls[right]) - walls[bottom]
        width = right - left - 1

        if height > 0:
            ans += height * width

    stack.append(i)

print(ans)