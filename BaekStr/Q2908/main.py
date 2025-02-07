# 두 상수 A, B가 주어 진다. 이 상수 A, B를 뒤집어 비교 하고 비교한 수 중 큰 수를 출력한다.
A, B = (input().split())
print(max(A[::-1], B[::-1]), end="")