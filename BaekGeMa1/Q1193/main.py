# 지그 재그로 분수를 출력 하자
# 1은 1개 2는 2개 3은 3개 씩 늘어 난다.
# 몇 번 째 줄에 위치 하나? X가 입력 값 이라면 X > n(n+1)/2 => n+1 값
# 이전 줄 까지의 합 n(n-1)/2 을 빼면 지금 줄의 순서를 알 수 있음
# 이 값을 X - n(n-1)/2 즉 pos 라고 지칭
# 홀수 줄: 분자가 n - pos + 1, 분모는 pos
# 짝수 줄: 분자가 pos, 분모는 n - pos + 1

X = int(input())

n = 1
while X > n * (n + 1) // 2:
    n += 1

pos = X - n * (n - 1) // 2
ext = n - pos + 1
if n % 2 == 0:
    print(pos,end="/")
    print(ext)
else:
    print(ext,end="/")
    print(pos)