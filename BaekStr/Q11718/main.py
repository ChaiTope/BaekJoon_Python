# 입력 받은 그대로 출력
import sys

print(sys.stdin.read(), end="")
# EOF 처리를 하는게 핵심. read() 는 계속 입력 받고, readline()은 한 줄만 입력 받음.