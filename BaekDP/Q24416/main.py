N = int(input())

count1, count2 = 0, 0
def fib(n):
    global count1
    if n == 1 or n == 2:
        count1 += 1
    else:
        fib(n - 1)
        fib(n - 2)

def fibonacci(n):
    global count2
    for i in range(3, n+1):
        count2 += 1
    return count2

count1_table = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
                55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181,
                6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418,
                317811, 514229, 832040, 1346269, 2178309, 3524578,
                5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155]
print(count1_table[N], N-2)

#아 개 열받아 왜 이딴게 풀이?