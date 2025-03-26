def pibonachi(repeat):

    num1, num2 = 0, 1
    for i in range(repeat):
        num1, num2 = num2, num1 + num2

    return num1