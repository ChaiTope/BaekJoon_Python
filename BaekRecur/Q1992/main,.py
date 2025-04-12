N = int(input())

paper = [list(map(int, input().strip())) for _ in range(N)]

def tree(arr, a, b, length):

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
        print(base, end="")

    else:
        print("(", end="")

        half = length // 2

        # 첫 줄 자르기
        tree(arr, a, b, half)
        tree(arr, a, b + half, half)

        # 둘째 줄 자르기
        tree(arr, a + half, b, half)
        tree(arr, a + half, b + half, half)

        print(")", end="")

tree(paper, 0, 0, N)