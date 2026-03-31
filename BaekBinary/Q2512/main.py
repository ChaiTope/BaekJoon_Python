import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
array = Counter(sorted(map(int, input().split())))
M = int(input())

summary = 0 # 지금까지 사용한 총 예산
h = N   # 아직 상한선에 걸리지 않은 지방 수
c = 0   # 이전 실제 상한선
answer = 0

for k, v in array.items():
    diff = k - c    # 이전 상한선에서 현재 예산값까지 올려야 하는 높이
    need = diff * h # 그 높이만큼 전체를 올리는 데 필요한 비용

    if summary + need > M:  # 여기까지 다 못 올리면
        answer = c + (M - summary) // h
        break

    summary += need # 여기까지 올릴 수 있으면 반영
    c = k   # 이전 상한선을 현재 값으로 갱신
    h -= v  # 현재 값 이하인 지방들은 이제 제외
    answer = k

print(answer)