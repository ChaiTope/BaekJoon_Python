a, b, c = int(input()), int(input()), int(input())

result = list(str(a * b * c))

nums = [0] * 10

for i in range(10):
    for j in result:
        if i == int(j):
            nums[i] = nums[i] + 1

for i in range(10):
    print(nums[i])