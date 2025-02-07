# 첫 번째 줄에는 테스트 케이스 개수 T가 주어 진다.
# 각 케이스 에는 반복 횟수 R 과 문자열 S 가 주어 진다.
import char

print("\n".join("".join(char * int(R) for char in S) for R, S in [input().split() for _ in range(int(input()))]), end="")