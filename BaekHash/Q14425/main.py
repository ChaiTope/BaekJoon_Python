N, M = map(int, input().split())

arr1 = []
arr2 = []
count = 0
for i in range(N):
    arr1.append(str(input()))

enu_arr1 = {value: index for index, value in enumerate(arr1)}

for j in range(M):
    arr2.append(str(input()))

for k in arr2:
    if k in enu_arr1:
        count += 1

print(count)