N = int(input())
n = 0
nums = list(map(int, input().split()))
stack = []
res = [-1] * N


for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        res[stack.pop()] = nums[i]
    stack.append(i)

print(*res)