# 킹 1개 퀸 1개 룩 2개 비숍 2개 나이트 2개 폰 8개
# 순서 대로 갯수가 입력 되면 몇개를 더하고 빼야 하는 지 구하라
Pieces = [1, 1, 2, 2, 2, 8]
Chess = list(map(int, input().split()))

diff = []
for i in range(6):
    diff.append(Pieces[i] - Chess[i])

print(" ".join(map(str, diff)), end="")


"""백준 서버 문제로 채점이 안 됐었음"""
Pieces = [1, 1, 2, 2, 2, 8]
Chess = list(map(int, input().split()))

# zip()함수 사용 << 두 인덱스 를 하나로 묶어 주는 역할
diff = [p - f for p, f in zip(Pieces, Chess)]

print(" ".join(map(str, diff)), end="")