# 입력 받은 수 / 4 만큼의 long 을 출력 하고 끝에 int
a = int(input())
for i in range(0, a//4): print("long", end=" ")
print("int", end=" ")

"""
백준 다른 사람 코드 보고 배운점
print(int(input())//4*'long ' + 'int')
문자열 반복은 [n * String] 을 사용 하면 즉시 n번 만큼 반복
"""