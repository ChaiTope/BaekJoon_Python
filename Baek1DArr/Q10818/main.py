# N 개의 정수가 주어지고
# 이 N 개의 정수중에 최소값과 최대값을 공백을 주고 한줄로 출력
N = int(input())
arr = list(map(int, input().split()))
print(min(arr), max(arr)) # 배열의 최소값과 최대값을 바로 출력해줌