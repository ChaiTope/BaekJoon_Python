import sys

input = sys.stdin.readline

N, K = map(int, input().split())

nums = [i for i in range(2, N+1)]

is_prime = [True] * (N+1)

cnt = 0

for num in nums:
    i = 1
    if is_prime[num]:
        while num * i <= N:
            if is_prime[num*i]:
                is_prime[num*i] = False
                cnt += 1
                if cnt == K:
                    print(num * i)
                    sys.exit()
                i += 1
            else:
                i += 1