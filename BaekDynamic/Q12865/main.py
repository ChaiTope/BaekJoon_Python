import sys
input = sys.stdin.readline

N, K = map(int, input().split())
WV = [tuple(map(int, input().split())) for _ in range(N)]

# V[w]: 무게 한계 w일 때 얻을 수 있는 최대 가치
V = [0] * (K+1)

for i in range(N):
    wi, vi = WV[i]
    # 뒤에서부터 순회해야 이전 단계 값을 덮어쓰지 않음
    for w in range(K, wi-1, -1):
        # 물건 i를 넣었을 때 vs 안 넣었을 때 중에 최대값
        V[w] = max(V[w], V[w-wi] + vi)

print(V[K])