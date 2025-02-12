# 가로, 세로 크기가 100인 흰 색종이 가 있다.
# 이 색종이 위에 T개의 10* 10 크기의 검은 색 종이를 한장 또는 여러 장 붙인다.
# 그 후 검은 색 종이 들의 넓이를 구하라

# 입력은 종이의 수, 그리고 종이의 수 만큼 X축과 Y축을 입력 받는다.

# 흰 색에서 검은색 종이가 덮일 때 마다 지우면 되지 않을까?

W = [[0]*100 for i in range(100)]
count = 0
T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            if W[j][k] != 1:
                W[j][k] = 1
                count+=1
print(count)


"""GPT 의 훈수"""
W = set()  # 덮인 좌표를 저장할 집합
T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            W.add((j, k))  # 중복되지 않는 좌표만 저장

print(len(W))  # 색종이가 덮인 총 면적 개수 출력

"""
set()을 사용하면 중복체크가 더 빠르다고 함
시간복잡도는 같지만, 공간복잡도가 더 효율적이라고 함
"""