import sys

def split(array, start, end):
    point = (end - start) // 3
    if end - start >= 3:
        for j in range(start + point, start + point*2):
            array[j] = ' '
        split(array, start, start + point)
        split(array, start + point*2, end)
    else:
        return

for line in sys.stdin:
    N = int(line)

    arr1 = ["-"]*(3**N)

    split(arr1, 0, len(arr1))

    print(''.join(arr1))