from math import gcd

a, x = map(int, input().split())
b, y = map(int, input().split())

gcd = gcd((a*y)+(b*x), (x*y))

print(((a*y)+(b*x))//gcd, (x*y)//gcd)