# B진법 수 N이 주어 진다. 이 수를 10진법 으로 바꾸자

N, B = map(str, input().split())

print(int(N, int(B))) # int(N, B)를 사용 하면 B 진수 N 을 10진수 로 풀어 줌