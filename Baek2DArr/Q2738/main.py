# 2차원 배열 첫 문제. 행렬 덧셈
# N*M 크기의 두 행렬 A, B가 주어 졌을 때 두 행렬을 더해라!
N,M = map(int, input().split())

A = [[0]*M for _ in range(N)]
B = [[0]*M for _ in range(N)]
for i in range(N):
    T = list(map(int, input().split()))
    for j in range(M):
        A[i][j] = T[j]
for i in range(N):
    T = list(map(int, input().split()))
    for j in range(M):
        B[i][j] = T[j]
for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j], end=" ")
    print()

"""GPT 의 개선 코드"""
N, M = map(int, input().split())

# 바로 2차원 리스트로 입력 받기
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

# 두 행렬을 더한 결과 출력
for i in range(N):
    print(*[A[i][j] + B[i][j] for j in range(M)])
