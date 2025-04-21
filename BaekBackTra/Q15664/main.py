from collections import Counter

N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
counter = Counter(arr)

unique_nums = sorted(counter.keys())
path = []

def backtrack(depth, start):
    if depth == M:
        print(' '.join(map(str, path)))
        return

    for i in range(start, len(unique_nums)):
        num = unique_nums[i]
        if counter[num] > 0:
            counter[num] -= 1
            path.append(num)
            backtrack(depth + 1, i)  # i부터 시작: 오름차순
            path.pop()
            counter[num] += 1

backtrack(0, 0)
