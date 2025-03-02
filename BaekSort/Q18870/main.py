import sys

N = int(input())
inp = list(map(int, sys.stdin.readline().split()))

# 중복 제거 + 정렬 (O(N log N))
sorted_unique = sorted(set(inp))

# 리스트 → 딕셔너리 변환 (O(N))
compression_map = {value: index for index, value in enumerate(sorted_unique)}

# 입력 리스트를 압축된 값으로 변환 (O(N))
sol = [compression_map[num] for num in inp]

# 결과 출력
sys.stdout.write(" ".join(map(str, sol)) + "\n")