N, K = map(int, input().split())
arr = []
for i in range(1, N+1):
    if N % i == 0:
        arr.append(i)
if len(arr) >= K:
    print(arr[K-1])
else:
    print(0)


### 개선 코드
N, K = map(int, input().split())
count = 0

# 약수는 sqrt(N)까지만 탐색

for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        # i는 약수
        count += 1
        if count == K:
            print(i)
            break

        # N // i도 약수 (중복 방지)
        if i != N // i:
            count += 1
            if count == K:
                print(N // i)
                break
else:
    print(0)
