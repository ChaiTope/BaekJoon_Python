N = int(input())

sqr = [["*"] * (N//3) for _ in range(N//3)]

def erase(arr, start, end):
    if end - start >= 3:
        val = (end-start)//3
        for i in range(start+val, start+val*2):
            for j in range(start+val, start+val*2):
                arr[i][j] = ' '

        erase(arr, start, start+val)
        erase(arr, start, start+val*2)
        erase(arr, start, start+val*3)
        erase(arr, start+val, start+val*2)
        erase(arr, start+val, start+val*2)
        erase(arr, start+val, start+val*3)
        erase(arr, start+val*2, end-val)
        erase(arr, start+val*2, end-val*2)
        erase(arr, start+val*2, end-val*3)
    else:
        return

erase(sqr, 0, len(sqr))

for row in sqr:
    print("".join(row))