import sys

input = sys.stdin.readline

nums = 0

for i in range(3):
    n = input().rstrip()
    if n.isdigit():
        nums = int(n) + 3 - i

if nums % 3 == 0 and nums % 5 == 0:
    print("FizzBuzz")
elif nums % 3 == 0:
    print("Fizz")
elif nums % 5 == 0:
    print("Buzz")
else:
    print(nums)