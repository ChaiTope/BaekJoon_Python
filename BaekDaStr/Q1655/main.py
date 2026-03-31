import sys
import heapq

input = sys.stdin.readline

left = []   # max heap (음수)
right = []  # min heap

for _ in range(int(input())):
    x = int(input())

    #  넣기
    if not left or x <= -left[0]:
        heapq.heappush(left, -x)
    else:
        heapq.heappush(right, x)

    # 균형 맞추기
    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))

    if len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))

    # 출력 (중앙값)
    print(-left[0])