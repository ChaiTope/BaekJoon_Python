import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

villages = []
houses = []
chickens = []

for i in range(N):
    house = list(map(int, input().split()))
    villages.append(house)

    for j in range(N):
        if house[j] == 1:
            houses.append((i, j))
        elif house[j] == 2:
            chickens.append((i, j))

chicken_combs = list(combinations(chickens, M))

min_city_dist = float('inf')

for combo in chicken_combs:        # combo는 M개의 (x,y) 좌표 튜플
    city_dist = 0
    for hx, hy in houses:          # 각 집마다
        # combo 안의 치킨집들까지의 맨해튼 거리를 전부 계산해서
        # 그 중 가장 작은 것 하나만 골라 더해 준다
        house_to_chicken = min(
            abs(hx - cx) + abs(hy - cy)
            for (cx, cy) in combo
        )
        city_dist += house_to_chicken

    # 이 조합으로 만든 도시 치킨 거리의 최솟값을 갱신
    if city_dist < min_city_dist:
        min_city_dist = city_dist

print(min_city_dist)
