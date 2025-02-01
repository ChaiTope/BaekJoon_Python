a = int(input())
result = []
for i in range(a):  # ✅ range(0, a)로 수정 (1부터 시작 X)
    b, c = map(int, input().split())
    result.append(b + c)

for j in range(a):  # ✅ 0부터 시작
    print(f"Case #{j+1}: {result[j]}")