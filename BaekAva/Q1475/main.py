import sys
import math
from collections import Counter

input = sys.stdin.readline

nums = Counter(map(int, input().strip()))

max_count = 0

if nums[6]:
    max_count += nums[6]
if nums[9]:
    max_count += nums[9]

max_count = math.ceil(max_count/2)

nums[6] = 0
nums[9] = 0

max_count = max(max_count, max(nums.values()))

print(max_count)