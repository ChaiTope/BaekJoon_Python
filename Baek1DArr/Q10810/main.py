# N 개의 바구니 M 번 반복 해서 공을 넣음
# 각 반복 에서는 시작 바구니, 마지막 바구니, 공의 번호를 입력
# 만약 그 바구니 에 이미 공이 존재 하면, 새로 입력 받은 공으로 교체
# 1번 바구니 부터 N 번 바구니 에 들어 있는 공의 번호를 공백 으로 구분해 출력
N, M = map(int, input().split())
baskets = [0] * N

# M번 작업 반복
for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i - 1, j):
        baskets[idx] = k

# 최종 바구니 상태 출력
print(" ".join(map(str, baskets)))
