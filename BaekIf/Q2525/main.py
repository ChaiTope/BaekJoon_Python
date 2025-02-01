# 시간 더하기 (오븐 시계)
a, b = map(int, input().split())
t = int(input())
if b + t < 60: print(a, b + t) # 두 분의 합이 60 이하일 때
else:
    if b + t < 120: # 시간에 + 1 하는 경우
        if a == 23: print(0, b + t - 60) # a == 23이면
        else : print(a + 1, b + t - 60) # 그 외에 경우
    else:
        if a + ((b + t) // 60) < 24: print(a + ((b + t)//60), (b + t) % 60) # 시간에 두 분의 합을 60으로 나눈 값이 23보다 작으면
        else: print(a + ((b + t)//60) - 24, (b + t) % 60)