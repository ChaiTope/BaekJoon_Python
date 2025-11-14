# kruskal_with_comment.py
# ------------------------
# 최소 스패닝 트리(MST) - Kruskal 알고리즘 구현

# ⚙️ 유니온 파인드 (Union-Find)
def find(parent, x):
    # 경로 압축
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    # 두 노드의 루트 노드를 합침
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# ⚙️ 메인 로직
def kruskal(n, edges):
    """
    n: 노드 개수
    edges: [(a, b, cost), ...] 형태의 간선 리스트
    return: MST의 총 비용, 그리고 MST에 포함된 간선 목록
    """
    # 1️⃣ 부모 테이블 초기화
    parent = [i for i in range(n + 1)]

    # 2️⃣ 간선을 비용 기준으로 정렬
    edges.sort(key=lambda x: x[2])

    total_cost = 0
    mst_edges = []

    # 3️⃣ 간선 하나씩 확인하며 MST 구성
    for a, b, cost in edges:
        # 사이클이 생기지 않으면 간선 포함
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost
            mst_edges.append((a, b, cost))

    return total_cost, mst_edges


#------------------------------------------------------------------

# ⚙️ 사용 예시
if __name__ == "__main__":
    # 노드 개수 N, 간선 개수 M
    N, M = 7, 9
    edges = [
        (1, 2, 29),
        (1, 5, 75),
        (2, 3, 35),
        (2, 6, 34),
        (3, 4, 7),
        (4, 6, 23),
        (4, 7, 13),
        (5, 6, 53),
        (6, 7, 25)
    ]

    total, mst = kruskal(N, edges)
    print("MST 총 비용:", total)
    print("MST 간선:", mst)


# kruskal_clean.py
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal(n, edges):
    parent = [i for i in range(n + 1)]
    edges.sort(key=lambda x: x[2])
    total_cost = 0
    mst_edges = []
    for a, b, cost in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total_cost += cost
            mst_edges.append((a, b, cost))
    return total_cost, mst_edges

if __name__ == "__main__":
    N, M = 7, 9
    edges = [
        (1, 2, 29),
        (1, 5, 75),
        (2, 3, 35),
        (2, 6, 34),
        (3, 4, 7),
        (4, 6, 23),
        (4, 7, 13),
        (5, 6, 53),
        (6, 7, 25)
    ]
    total, mst = kruskal(N, edges)
    print(total)
    print(mst)
