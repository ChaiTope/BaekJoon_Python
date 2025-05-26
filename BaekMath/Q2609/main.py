import math

a, b = map(int, input().split())

# 최대 공약수, 최소 공배수 구하는 함수
print(math.gcd(a, b))
print(math.lcm(a, b))

# 유클리드 호재법
c, d = a, b
while d:
    c, d = d, c % d
print(c)


print(a*b//c)