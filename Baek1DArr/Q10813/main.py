# N개의 바구니, 그리고 N번 까지의 공이 순차적 으로 들어 있다.
# M번 공을 바꿀 예정 각 줄에는 두 정수가 입력, 그 두 정수에 해당 하는 공을 교환

# 작업 완료 후 1번 부터 N번 까지의 바구니 안의 공을 출력

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(i+1)

for i in range(m):
    a, b = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]

for i in range(len(arr)):
    if i == len(arr)-1:
        print(arr[i], end="")
        break
    print(arr[i], end=" ")

"""GPT 의 개선 및 최적화"""
n, m = map(int, input().split())
arr = list(range(1, n + 1))  # ✅ 리스트 초기화 간결하게!

for _ in range(m):
    a, b = map(int, input().split())
    arr[a - 1], arr[b - 1] = arr[b - 1], arr[a - 1]  # ✅ Pythonic한 swap 유지

print(" ".join(map(str, arr)))  # ✅ join() 사용하여 마지막 공백 문제 해결!