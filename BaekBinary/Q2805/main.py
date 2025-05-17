import sys

input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))

def enough(H):
    # H 높이로 자를 때 얻는 나무 길이 합
    total = sum((a - H) for a in trees if a > H)
    return total >= M

L, R = 0, max(trees)
ans = 0
while L <= R:
    mid = (L + R) // 2
    if enough(mid):
        ans = mid        # mid로도 M 이상 얻을 수 있으니 기억
        L = mid + 1      # 더 높은 H도 시도해보기
    else:
        R = mid - 1      # 너무 높아서 나무가 모자라면 낮춰야 함
print(ans)
