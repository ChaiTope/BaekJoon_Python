import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int, input().split())

array = sorted(list(input().split()))

comb = combinations(array, L)

for c in comb:
    vowel = 0
    consonant = 0

    for x in c:
        if x in "aeiou":
            vowel += 1
        else:
            consonant += 1

    if vowel >= 1 and consonant >= 2:
        print("".join(c))