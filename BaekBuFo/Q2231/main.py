# 최적화 후 코드
N = int(input())

for i in range(1, N+1):
    sum1 = sum(map(int, str(i)))
    if sum1 + i == N:
        print(i)
        break
else:
    print(0)
