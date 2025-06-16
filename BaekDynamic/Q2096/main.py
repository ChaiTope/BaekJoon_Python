import sys
input = sys.stdin.readline

N = int(input())

a, b, c = map(int, input().split())
prev_max = [a, b, c]
prev_min = [a, b, c]

for _ in range(N-1):
    a, b, c = map(int, input().split())

    # 이번 행의 최댓값
    cur_max0 = a + max(prev_max[0], prev_max[1])
    cur_max1 = b + max(prev_max)
    cur_max2 = c + max(prev_max[1], prev_max[2])

    # 이번 행의 최솟값
    cur_min0 = a + min(prev_min[0], prev_min[1])
    cur_min1 = b + min(prev_min)
    cur_min2 = c + min(prev_min[1], prev_min[2])

    # 다음 반복을 위해 덮어쓰기
    prev_max = [cur_max0, cur_max1, cur_max2]
    prev_min = [cur_min0, cur_min1, cur_min2]

# 마지막 줄 결과만 남아있음
print(max(prev_max), min(prev_min))
