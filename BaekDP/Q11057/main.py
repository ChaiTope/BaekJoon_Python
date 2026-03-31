N = int(input())
res = 1
r = min(N, 9)

for i in range(N+9, N+9-r, -1):
    res *= i
for i in range(1, r+1):
    res //= i

print(res%10007)