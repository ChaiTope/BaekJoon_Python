import sys
sys.setrecursionlimit(10**7)

pre = []
while True:
    try:
        line = sys.stdin.readline().strip()
        if not line:
            break        # 빈 줄이 들어오면 멈추는 경우
        num = int(line)
        pre.append(num)
    except EOFError:  # 더 이상 읽을 게 없을 때
        break


def pre_to_post(pre):
    if not pre: return []
    root = pre[0]
    # 루트보다 큰 첫 인덱스 찾기
    split = next((i for i, v in enumerate(pre) if v > root), len(pre))
    left_pre = pre[1:split]
    right_pre = pre[split:]
    left_post = pre_to_post(left_pre)
    right_post = pre_to_post(right_pre)
    return left_post + right_post + [root]

for i in pre_to_post(pre):
    print(i)