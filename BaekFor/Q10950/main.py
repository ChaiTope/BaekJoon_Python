#반복할 횟수를 받고, 두 수를 그만큼 반복해서 입력받은 후 결과를 출력
a = int(input())
res = []
for i in range(a):
    b, c = map(int, input().split())
    res.append(b + c)

for j in range(a):
    print(res[j])