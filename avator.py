N = int(input())
A = list(map(int, input().split()))

arr = []

for i in range(N):
    arr.append((A[i], i))   # 값, 원래 인덱스

arr.sort()

P = [0] * N

for sorted_idx in range(N):
    value, original_idx = arr[sorted_idx]
    P[original_idx] = sorted_idx

print(*P)