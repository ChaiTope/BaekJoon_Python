import sys
from bisect import bisect_right

input = sys.stdin.readline

N, M, K = map(int, input().split())
cards = list(map(int, input().split()))
queries = list(map(int, input().split()))

cards.sort()

# DSU: parent[i] = i번 인덱스 카드가 사용됐으면 "다음 후보 인덱스"를 가리키게 함
# 마지막 처리를 위해 M까지(=없음) 한 칸 더 둠
parent = list(range(M + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def use(i):
    # i번 카드를 사용했으니 다음 카드로 연결
    parent[i] = find(i + 1)

out = []
for x in queries:
    # x보다 큰 카드의 첫 위치
    idx = bisect_right(cards, x)
    idx = find(idx)    # 이미 사용됐을 수도 있으니 DSU로 점프
    out.append(str(cards[idx]))
    use(idx)

print("\n".join(out))