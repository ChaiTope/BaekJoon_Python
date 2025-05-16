import sys

input = sys.stdin.readline

N, M = map(int, input().split())

link = {}
for i in range(N):
    site, password = input().split()

    link[site] = password

for j in range(M):
    site = input().rstrip()
    print(link[site])