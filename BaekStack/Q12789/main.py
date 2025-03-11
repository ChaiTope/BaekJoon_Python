n = int(input())

way = list(map(int, input().split()))
stay = []
while way:
    if way[0] == min(way): # 만약 첫 번째가 가장 작은 수라면
        if stay: # 대기실에 사람이 있으면
            if stay[-1] > min(way): # 대기실의 마지막 사람이 줄의 첫 사람보다 크면
                way.remove(min(way)) # 줄의 첫 사람을 없앰
            elif stay[-1] == min(stay):
                stay.remove(stay[-1]) # 아니면 대기실의 마지막 사람을 없앰
            else:
                stay.append(way[0])
                way.remove(way[0])

        else:
            way.remove(way[0]) # 대기실에 사람이 없으면 줄의 첫 사람을 없앰

    else: # 첫 번째 사람이 가장 작은 사람이 아니면
        if stay: # 대기실에 사람이 있으면
            if min(stay) < min(way): # 대기실의 가장 작은 수가 줄의 가장 작은 수보다 작으면
                if stay[-1] == min(stay):
                    stay.pop() # 그 사람을 없앰
                else:
                    break
            else:
                stay.append(way[0])
                way.remove(way[0])
        else:
            stay.append(way[0])
            way.remove(way[0])

    print(way, stay)

while not way and stay:
    if stay[-1] == min(stay):
        stay.pop()
    else:
        break

if way or stay:
    print("Sad")
else:
    print("Nice")