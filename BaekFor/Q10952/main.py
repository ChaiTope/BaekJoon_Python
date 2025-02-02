result = []
a , b = 1, 1
while a != 0 or b != 0:
    a, b = map(int, input().split())
    if a == b == 0: break
    result.append(a + b)
for i in range(0, len(result)):
    if len(result) - 1 == i:
        print(result[i], end="")
    else:
        print(result[i])

"""
새로 배운 점, len()로 배열의 길이를 즉시 사용 가능
"""

"""
GPT 가 최적화 한 코드
"""
result = []
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    result.append(str(a + b))  # ✅ 문자열로 변환하여 join 가능

# ✅ `"\n".join()` 사용 → `print()` 호출 1번만 실행 (속도 개선)
print("\n".join(result))