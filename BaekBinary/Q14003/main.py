import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
tails_val = []
tails_idx = []
prev = [-1] * N
pos = [0] * N

for i in range(N):
    num = nums[i]

    if not tails_val or num > tails_val[-1]:
        prev[i] = tails_idx[-1] if tails_idx else -1
        tails_val.append(num)
        tails_idx.append(i)
        pos[i] = len(tails_val) - 1

    else:
        l = 0
        r = len(tails_val)

        while l < r:
            mid = (l + r) // 2
            if tails_val[mid] < num:
                l = mid + 1
            else:
                r = mid

        tails_val[l] = num
        tails_idx[l] = i
        pos[i] = l
        prev[i] = tails_idx[l-1] if l > 0 else -1

result = []
L = len(tails_val)
print(L)
cur = tails_idx[L-1]

while cur != -1:
    result.append(nums[cur])
    cur = prev[cur]

result = list(reversed(result))
print(*result)