N = int(input())
count_dict = {}

for _ in range(N):
    num = int(input())
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print(count_dict)
