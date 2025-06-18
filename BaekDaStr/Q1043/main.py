import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
truth = list(map(int, input().split()))

# 진실을 아는 사람 집합
peoples = [False]*(N+1)
for p in truth[1:]:
    peoples[p] = True

# 파티별 참석자만 담기
parties = []
for _ in range(M):
    data = list(map(int, input().split()))
    parties.append(data[1:])   # data[0]은 인원수

# 반복 스캔으로 진실 전파
changed = True
while changed:
    changed = False
    for party in parties:
        if any(peoples[p] for p in party):
            for p in party:
                if not peoples[p]:
                    peoples[p] = True
                    changed = True

# 거짓말 가능한 파티 개수
ans = sum(1 for party in parties if not any(peoples[p] for p in party))
print(ans)
