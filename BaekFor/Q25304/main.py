# 내가 받은 영수증이 옳게 된 영수증인가
# 첫 번째 줄에는 총 가격, 두 번째 줄에는 물건의 종류 수
# 그 후에는 각 물건의 가격과 갯수
# 각 물건의 가격과 갯수를 모두 더한 값이 총 가격과 같으면 Yes, 아니면 No

total = int(input())
count = int(input())
price = 0
for i in range(count):
     a, b = map(int, input().split())
     price += (a * b)

if total == price:
    print("Yes")
else:
    print("No")