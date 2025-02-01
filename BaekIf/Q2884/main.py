#한줄로 시간 분 입력받으면 -45분해서 출력 60 - 45 - b
a, b = map(int, input().split())
if b < 45:
    if a == 0 : print(23,b+15)
    else: print(a-1,b+15)
else: print(a,b-45)