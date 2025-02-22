# 입 출금을 할 횟수를 N, 이후에 입금 또는 출금할 수, 행동 이후의 잔액을 한 줄에 입력(입금은 양수, 출금은 -를 붙인 음수)
# 해당 행위를 위해 필요한 최소값 출력
# 출력값일 때만 최소값을 찾을 수 있음. 일단 다 배열에 저장해야 할 것 같은데, 이러면 시간이 되나?
# 공약수를 구하는 것이 핵심.근데 공약수를 어떻게 구해야하나...
import math

N = int(input())
res = []
val = []
ori = []
count = 0

while count < N:
    A, B = map(int, input().split())
    ori.append(A)
    if A > 0:
        res.append(B)
    else:
        if count > 0 and len(res) > count - 1:
            res.append(B)
            val.append(B + (-A) - res[count - 1])
        else:
            val.append(1)
            val.append(-A)
    count += 1

if not val:
    print(-1)
elif sum(ori) >= 0 and all(x == 0 for x in res):
    print(0)
elif sum(ori) < 0 and all(x == 0 for x in res):
    print(-1)
else:
    val = [x for x in val if x != 0]
    gcd = []
    if len(val) > 1:
        for i in range(len(val) - 1):
            gcd.append(math.gcd(val[i], val[i+1]))

    if not gcd and val:
        res_filtered = [x for x in res if x != 0]
        if res_filtered:
            gcd.append(min(res_filtered))

    if not gcd or min(gcd) == 1:
        print(-1)
    else:
        print(min(gcd))


    print(gcd)

print(res)
print(val)