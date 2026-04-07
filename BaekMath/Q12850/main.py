D = int(input())
mod = 10 ** 9 + 7
A = [[0,1,1,0,0,0,0,0],
     [1,0,1,1,1,0,0,0],
     [1,1,0,0,1,0,0,0],
     [0,1,0,0,1,1,1,0],
     [0,1,1,1,0,0,1,0],
     [0,0,0,1,0,0,0,1],
     [0,0,0,1,1,0,0,1],
     [0,0,0,0,0,1,1,0]]

def mm(x, y):
    Z = [[0 for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            temp = 0
            for k in range(8):
                temp += x[i][k] * y[k][j]
            Z[i][j] = temp % mod
    return Z

def mat_pow(A, d):
    if d == 1:
        return A

    half = mat_pow(A, d//2)

    if d % 2 == 0:
        return mm(half, half)
    else:
        return mm(mm(half, half), A)
result = mat_pow(A, D)
print(result[0][0])