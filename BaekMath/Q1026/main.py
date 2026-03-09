N = int(input())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())), reverse=True)
S = 0
for i in range(N):
    S += arr1[i] * arr2[i]
print(S)