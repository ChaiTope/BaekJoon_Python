import sys

input = sys.stdin.readline

N = int(input())

square = [[0]*N for i in range(N)]

coo = []
result_list = []
for i in range(N):
    nums = list(map(int, input().rstrip()))
    for j in range(N):
        square[i][j] = nums[j]
        if nums[j] == 1:
            coo.append([i,j])

visited = [[False] * N for _ in range(N)]

x_way = [-1,1,0,0]
y_way = [0,0,-1,1]

def complex(x, y, path):
    if visited[x][y]:
        return

    visited[x][y] = True
    path.append([x,y])

    for dir in range(4):
        nx = x + x_way[dir]
        ny = y + y_way[dir]

        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and square[nx][ny] == 1:
                complex(nx, ny, path)

for c in coo:
    if not visited[c[0]][c[1]]:
        group = []                  # 이 리스트에 좌표들이 쌓일 거고
        complex(c[0], c[1], group)  # 재귀 돌리면서 group에 [x,y]를 추가
        houses = len(group)    # 함수를 빠져나온 뒤, group 길이가 집 개수
        result_list.append(houses)

result_list = sorted(result_list)
print(len(result_list))
for value in result_list:
    print(value)