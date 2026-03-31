import heapq
N = int(input())
A = list(map(int, input().split()))
heapq.heapify(A)

for i in range(1, N):
    for j in list(map(int, input().split())):
        if A[0] < j:
            heapq.heapreplace(A, j)

print(A[0])