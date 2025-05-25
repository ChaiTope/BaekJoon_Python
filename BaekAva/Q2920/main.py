default = [1, 2, 3, 4, 5, 6, 7, 8]
reverse = list(reversed(default))
array = list(map(int, input().split()))

if array == default:
    print("ascending")
elif array == reverse:
    print("descending")
else:
    print("mixed")