N = int(input())

des = 0
n = 0
while True:
    des += 1
    if "666" in str(des):
        n += 1

    if n == N:
        print(des)
        break