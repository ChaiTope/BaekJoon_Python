N = int(input())

paper = [list(map(int, input().split())) for i in range(N)]

plus = 0
zero = 0
minus = 0

def cutting(arr, a, b, length):
    global minus, zero, plus
    base = arr[a][b]
    same = True
    for i in range(a, a + length):
        for j in range(b, b + length):
            if arr[i][j] != base:
                same = False
                break
        if not same:
            break

    if same:
        if base == 0:
            zero += 1
        elif base == 1:
            plus += 1
        else:
            minus += 1

    else:
        third = length // 3

        # 첫 줄 자르기
        cutting(arr, a, b, third)
        cutting(arr, a, b + third, third)
        cutting(arr, a, b + third*2, third)

        # 둘째 줄 자르기
        cutting(arr, a + third, b, third)
        cutting(arr, a + third, b + third, third)
        cutting(arr, a + third, b + third*2, third)

        # 셋째 줄 자르기
        cutting(arr, a + third*2, b, third)
        cutting(arr, a + third*2, b + third, third)
        cutting(arr, a + third*2, b + third*2, third)


cutting(paper, 0, 0, N)
print(minus)
print(zero)
print(plus)