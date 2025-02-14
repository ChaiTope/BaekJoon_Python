# 진법 변환 2
# 10 진법 N 이 주어 진다. 이 수를 B 진법 으로 바꿔 출력 하라.
# 나눗셈 의 몫과 나머지를 활용 해야 한다.

N, B = map(int, input().split())

def base_change(N, B):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while N > 0:
        result = digits[N % B] + result
        N //= B
    return result

print(base_change(N, B))
