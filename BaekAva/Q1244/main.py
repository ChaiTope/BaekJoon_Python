import sys
input = sys.stdin.readline

N = int(input())

SW = [0] + list(map(int, input().split()))

M = int(input())

def boy(n):
    k = n
    while k <= N:
        SW[k] ^= 1
        k += n

def girl(n):
    l = r = n
    # 양쪽이 범위 안이고, 값이 같을 때만 확장
    while l - 1 >= 1 and r + 1 <= N and SW[l - 1] == SW[r + 1]:
        l -= 1
        r += 1

    # 확정된 구간 토글
    for i in range(l, r + 1):
        SW[i] ^= 1

for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        boy(b)
    else:
        girl(b)

# 출력은 20개씩 끊기
for i in range(1, N + 1):
    print(SW[i], end=" ")
    if i % 20 == 0:
        print()
