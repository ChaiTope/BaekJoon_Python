arr = []
for i in range(5):
    arr.append(int(input()))

arr.sort()
print((arr[1] + arr[2] + arr[3] + arr[4] + arr[0]) // 5)
print(arr[2])