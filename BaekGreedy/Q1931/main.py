import sys

input = sys.stdin.readline

N = int(input())

meeting = []
for i in range(N):
    m, t = map(int, input().split())

    meeting.append((t, m))

meeting = sorted(meeting)

count = 0
yet = 0

for m, t in meeting:
    if t >= yet:
        count += 1
        yet = m

print(count)