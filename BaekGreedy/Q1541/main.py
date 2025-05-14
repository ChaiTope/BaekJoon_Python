array = list(input())
middle = []

final = []
operator = []

for i in range(len(array)):
    if array[i] == "+" or array[i] == "-":
        final.append(int("".join(middle)))
        middle = []
        operator.append(array[i])
    elif i == len(array) - 1:
        middle.append(array[i])
        final.append(int("".join(middle)))
    else:
        middle.append(array[i])

is_plus = True
mid_sum = 0
summary = final[0]
for i in range(len(final)-1):
    if operator[i] == "-":
        is_plus = False

    if is_plus:
        summary -= mid_sum
        mid_sum = 0
        summary += final[i+1]
    else:
        mid_sum += final[i+1]
summary -= mid_sum
print(summary)