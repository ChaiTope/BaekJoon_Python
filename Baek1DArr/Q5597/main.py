# 1 부터 30까지의 중복 없는 랜덤수 중 28개가 부여
# 이 중 없는 두개를 찾기
arr = []
for i in range(28):
    a = int(input())
    arr.append(a)
for i in range(1, 31):
    if i in arr:
        continue
    else:
        print(i)

"""GPT 의 최적화 코드"""
arr = {int(input()) for _ in range(28)}  # ✅ 리스트 대신 집합(set) 사용

for i in range(1, 31):
    if i not in arr: # in else 대신 not in 사용
        print(i)