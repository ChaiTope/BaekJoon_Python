import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
fruits = list(map(int, input().split()))

count = defaultdict(int)   # 과일 종류별 개수를 셀 딕셔너리
left = 0
distinct = 0
answer = 0

for right in range(n):
    # right 포인터가 새 과일 하나를 가져온다
    if count[fruits[right]] == 0:
        distinct += 1
    count[fruits[right]] += 1

    # 만약 종류가 3개가 되면 left를 한 칸씩 옮겨서 다시 2종 이하로 맞춘다
    while distinct > 2:
        count[fruits[left]] -= 1
        if count[fruits[left]] == 0:
            distinct -= 1
        left += 1

    # 이 시점에는 항상 distinct ≤ 2가 보장되므로, 구간 길이를 갱신
    answer = max(answer, right - left + 1)

print(answer)
