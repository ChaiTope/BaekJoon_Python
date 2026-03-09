array = []
for i in range(5):
    n = int(input())
    if n < 40:
        array.append(40)
        continue
    array.append(n)
print(sum(array)//5)