# 벌집 에서 최단 거리 구하기
# 벌집 크기의 규칙은 (n-1)*6 씩 더해 진다는 것 (i-1)*6
# 그러면 13이 주어 지면 어떻게 최단 거리를 구하지?
import sys
n = int(sys.stdin.readline())
i = 1
while 1+(i-1)*6 < n:
    n -= (i-1)*6
    i += 1
print(i) # 와 이걸 풀었네 ㄹㅇ 난 천재인 듯

"""등차 수열을 이용 해서 구하면"""
import math
n = int(input())

if n == 1:
    print(1)
else:
    layer = 1
    while n > 1 + 6 * layer * (layer - 1) // 2:
        layer += 1
    print(layer)