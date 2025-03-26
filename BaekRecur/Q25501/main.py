import sys

N = int(input())

def isPalindrome(char, count):
    count += 1
    if len(char) == 1 or len(char) == 0:
        return 1, count
    elif char[0] == char[-1]:
        return isPalindrome(char[1:-1], count)
    else:
        return 0, count

for _ in range(N):
    print(" ".join(map(str, isPalindrome(sys.stdin.readline().strip(), 0))))