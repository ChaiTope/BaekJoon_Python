#Counter 활용
from collections import Counter

sqr1, sqr2 = [], []
for _ in range(3):
    x, y = map(int, input().split())
    sqr1.append(x)
    sqr2.append(y)
count1 = Counter(sqr1)
count2 = Counter(sqr2)
a = [key for key, value in count1.items() if value == 1]
b = [key for key, value in count2.items() if value == 1]
print(a[0], b[0])

#for문과 if문으로
a, b, c = [], [], []
for i in range(3):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

if a[0] == a[1]:
    c.append(a[2])
elif a[0] == a[2]:
    c.append(a[1])
else:
    c.append(a[0])
if b[0] == b[1]:
    c.append(b[2])
elif b[0] == b[2]:
    c.append(b[1])
else:
    c.append(b[0])

print(c[0], c[1])

#XOR 연산을 활용
x_list, y_list = [], []

for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x4 = x_list[0] ^ x_list[1] ^ x_list[2]
y4 = y_list[0] ^ y_list[1] ^ y_list[2]

print(x4, y4)

#zip을 활용 및 최대 최적화
sqr = [list(map(int, input().split())) for _ in range(3)]
x, y = zip(*sqr)

p1 = x[0] ^ x[1] ^ x[2]
p2 = y[0] ^ y[1] ^ y[2]
print(p1, p2)
