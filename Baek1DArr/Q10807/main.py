# 1. 입력받을 정수의 갯수 N을 입력받음
# 2. N개만큼 정수를 공백으로 구분해서 받음
# 3. 받은 정수중에 고를 수를 세번째 줄로 입력받음

# 출력은 세번째에 받은 수를 두번째에서 몇갠지 출력함

N = int(input())
arr = list(map(int, input().split()))
F = int(input())
count = 0
for i in range(len(arr)):
    if arr[i] == F:
        count += 1
print(count)

"""GPT 가 최적화 해준 코드"""
N = int(input())
arr = list(map(int, input().split()))
F = int(input())
print(arr.count(F))

"""만약 입력 값이 너무 많다면"""
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
F = int(input())
print(arr.count(F))