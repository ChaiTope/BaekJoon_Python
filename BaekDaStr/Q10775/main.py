import sys
input = sys.stdin.readline

G = int(input())   # 게이트 수
P = int(input())   # 비행기 수

parent = list(range(G + 1))  # 0은 "더 이상 없음" 센티널

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # path compression (halving)
        x = parent[x]
    return x

ans = 0
for _ in range(P):
    g = int(input())
    k = find(g)          # g 이하에서 가장 큰 빈 게이트
    if k == 0:           # 배정 불가 -> 즉시 종료
        break
    parent[k] = find(k - 1)  # k를 사용했으니 다음 후보는 k-1 쪽
    ans += 1

print(ans)
