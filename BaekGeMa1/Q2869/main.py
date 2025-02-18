# 와! 땅 위에 달팽이 가 있대요!
# 이 달팽이 가 높이 V 인 나무 막대를 올라 가고 싶대요!
# 달팽이 는 낮에 N 미터를 올라 가고, 밤에 B 미터 떨어 진다!
# 달팽이 가 나무 막대를 모두 올라 가려면 얼마나 걸릴까?
# 값은 A B V 가 공백 으로 구분 되어 주어 진다!
import math

# V - A를 했을 때, 남은 V가 0 보다 크다면 V + B, 작다면 종료

A,B,V = map(int,input().split())
count = 0
while True:
    V -= A
    count += 1
    if V > 0:
        V += B
    else:
        break
print(count)

# 위 코드는 시간 초과!!!!!!!
# 새로운 식(수학적 풀이)
# 하루에 실질적 으로 올라 가는 거리: A - B
# 도달 해야 하는 거리(정상 전 날까지): V - A (낮 한번 빼는거)
# 따라서 필요한 날 수 = (V - A)/(A - B)(반올림) + 1(하루 뺀거 다시 더하기)

A,B,V = map(int,input().split())
days = math.ceil((V-A)/(A-B)) + 1
print(days)