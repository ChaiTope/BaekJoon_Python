# 이전 문제와 같은 문제지만, EOF를 처리해야함
import sys
result = []
for line in sys.stdin:
    a, b = map(int, line.split())
    result.append(str(a + b))

print("\n".join(result), end="")

# ctrl + D 로 종료하면 결과가 출력됨