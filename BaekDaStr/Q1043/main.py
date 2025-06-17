import sys

input = sys.stdin.readline

N, M = map(int, input().split())

truth = list(map(int, input().split()))

if len(truth) == 1:
    print(M)
else:
    peoples = [0] * N

    parties = []
    for i in range(M):
        party = list(map(int, input().split()))
        parties.append(party)

        for people in party:
            if people in truth:
                #일단 여기까지
                peoples.remove(people)