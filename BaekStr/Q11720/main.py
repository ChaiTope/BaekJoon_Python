# N 개의 숫자가 공백 없이 입력 된다.
# 이 숫자를 모두 합해서 출력 한다.
N = int(input())
arr = list(input())
x = 0
for i in range(N):
    x += int(arr[i])
print(x, end="")

# int(input()) 과 map(int, input()) 의 차이점 확실히 이해