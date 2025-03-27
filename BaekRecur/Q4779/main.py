import sys

def erase(array):
    if len(array) == 1:
        return array
    else:
        for j in range(len(array)//3-1, len(array)//3*2):
            array[j] = []
        return array

def split(array):
    erase(array)

for line in sys.stdin:
    N = int(line)

    arr = ["-"]*(N**3)

    for i in range(N):
        arr = split(arr)
