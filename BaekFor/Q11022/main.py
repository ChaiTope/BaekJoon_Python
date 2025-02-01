a = int(input())
n, m = [],[]
for i in range(a):
    b, c = map(int, input().split())
    n.append(b)
    m.append(c)

for j in range(a):
    print(f"Case #{j+1}: {n[j]} + {m[j]} = {n[j]+m[j]}")

"""
f("")를 사용하면 {}로 변수를 직접 대입 가능 (JAVA의 th문처럼?)
"""