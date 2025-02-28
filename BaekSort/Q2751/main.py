import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

arr.sort()

sys.stdout.write("\n".join(map(str, arr)) + "\n")
