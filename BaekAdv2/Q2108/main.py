import sys
from collections import Counter

N = int(sys.stdin.readline())

nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))

avg = sum(nums) / len(nums)

sorted_nums = sorted(nums)

median = sorted_nums[len(sorted_nums) // 2]

counter = Counter(sorted_nums).most_common()

max_count = counter[0][1]

mode_candidates = [num for num, cnt in counter if cnt == max_count]

if len(mode_candidates) == 1:
    many = mode_candidates[0]
else:
    mode_candidates.sort()
    many = mode_candidates[1]

range_num = max(nums) - min(nums)

print(round(avg), median, many, range_num, sep='\n')