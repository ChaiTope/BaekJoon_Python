# 9 * 9 격자판 에 쓰여진 81개 의 자연수 또는 0 이 주어질 때
# 최대값 을 구하고 그 위치를 출력 해라

arr = [[0] * 9 for _ in range(9)]
for i in range(9):
    num = list(map(int, input().split()))
    for j in range(9):
        arr[i][j] = num[j]

max_i, max_j = 0, 0
max_value = -1

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_value:
            max_value = arr[i][j]
            max_i, max_j = i+1, j+1
print(max_value)
print(max_i, max_j)

"""일단 한번 다시 짜 본 코드"""

arr = [list(map(int, input().split())) for _ in range(9)] #<< 어차피 max()로 찾을 게 아니니 이렇게 받아도 됨

max_i, max_j = 0, 0
max_value = -1

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_value:
            max_value = arr[i][j]
            max_i, max_j = i+1, j+1

print(max_value)
print(max_i, max_j)