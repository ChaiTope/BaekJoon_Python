# 첫 줄에 입력 받을 갯수 N 정수 X 를 입력 받는다.
# 두 번째 줄에 N 개의 정수를 입력 받는다.
# N 개의 정수 중에 X 보다 작은 정수를 순서 대로 출력 한다.
N, X = map(int, input().split())
arr = list(map(int, input().split()))
sel_arr = []
for i in range(N):
    if arr[i] < X:
        sel_arr.append(arr[i])
"""
for i in sel_arr: # 배열이 끝날 때 까지 반복 << 틀림! 배열의 값을 i 가 순차적 으로 가짐
    if i == len(sel_arr)-1: # 배열의 마지막 요소
        print(i, end="")
        break
    print(i, end=' ')
"""

"""GPT 가 알려준 개선점"""

for idx in range(len(sel_arr)):
    if idx == len(sel_arr) - 1:
        print(sel_arr[idx], end="")
    else:
        print(sel_arr[idx], end=" ")