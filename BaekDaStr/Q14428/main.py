import sys

input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
M = int(input())

tree = [0] * (4 * N)

def build(node, start, end):
    if start == end:
        tree[node] = start   # 이 구간(한 칸)의 최소 인덱스는 자기 자신
    else:
        mid = (start + end) // 2
        build(node*2, start, mid)
        build(node*2+1, mid+1, end)

        left_idx = tree[node*2]
        right_idx = tree[node*2+1]

        if arr[left_idx] < arr[right_idx]:
            tree[node] = left_idx
        elif arr[left_idx] > arr[right_idx]:
            tree[node] = right_idx
        else:
            tree[node] = min(left_idx, right_idx)

def query(node, start, end, left, right):
    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_idx = query(node*2, start, mid, left, right)
    right_idx = query(node*2+1, mid + 1, end, left, right)

    if left_idx == 0 and right_idx == 0:
        return 0
    elif left_idx == 0:
        return right_idx
    elif right_idx == 0:
        return left_idx
    else:
        if arr[left_idx] < arr[right_idx]:
            return left_idx
        elif arr[left_idx] > arr[right_idx]:
            return right_idx
        else:
            return min(left_idx, right_idx)


def update(node, start, end, idx, val):
    if idx < start or idx > end:
        return

    if start == end:
        # 실제 값 갱신
        arr[idx] = val
        # 이 구간(한 칸)의 최소 인덱스는 자기 자신
        tree[node] = idx
        return

    mid = (start + end) // 2
    if idx <= mid:
        update(node * 2, start, mid, idx, val)
    else:
        update(node * 2 + 1, mid + 1, end, idx, val)

    left_idx = tree[node * 2]
    right_idx = tree[node * 2 + 1]

    if arr[left_idx] < arr[right_idx]:
        tree[node] = left_idx
    elif arr[left_idx] > arr[right_idx]:
        tree[node] = right_idx
    else:
        tree[node] = min(left_idx, right_idx)

build(1, 1, N)

for i in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 1, N, b, c)
        continue

    print(query(1, 1, N, b, c))