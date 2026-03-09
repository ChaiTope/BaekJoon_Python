array = [int(input()) for i in range(9)]

array = sorted(array)

target = sum(array) - 100
find = False

for i in range(9):
    for j in range(i + 1, 9):
        if array[i] + array[j] == target:
            array.remove(array[j])
            array.remove(array[i])
            find = True
            break
    if find:
        break

for num in array:
    print(num)