# 수를 입력 받고 1부터 그 수 까지 합을 구한다
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)