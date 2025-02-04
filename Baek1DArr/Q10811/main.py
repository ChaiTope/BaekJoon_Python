# N, M이 첫 줄에 주어 진다, 1 ~ N번 까지의 바구니 와 공이 생긴다
# i부터 j까지 바구니 들이 역순 으로 정렬 된다.
# 이 과정을 M 번 반복 하고 첫 공의 숫자 부터 끝까지 출력 한다.

N, M = map(int, input().split())
baskets = list(range(1, N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    baskets[i-1: j] = baskets[i-1: j][::-1] # [n, m] 리스트 슬라이싱 (n부터 m-1까지), [::-1]으로 역정렬
print(*baskets) # index 를 공백 기준 으로 나눠서 출력