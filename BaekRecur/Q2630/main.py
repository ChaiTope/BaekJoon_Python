N = int(input())

paper = [list(map(int, input().split())) for i in range(N)]

count1 = 0
count0 = 0

def cutting(arr, a, b, length):
    global count1, count0
    judge = []
    for i in range(a, a + length):
        for j in range(b, b + length):
            judge.append(arr[i][j])
            if i == a+length-1 and j == b+length-1:
                if len(set(judge)) > 1:
                    cutting(arr, a, b, length//2)
                    cutting(arr, a + length//2, b, length//2)
                    cutting(arr, a, b + length//2, length//2)
                    cutting(arr, a + length//2, b + length//2, length//2)
                else:
                    if judge[0] == 0:
                        count0 += 1
                    else:
                        count1 += 1
                    return

cutting(paper, 0, 0, N)
print(count0)
print(count1)