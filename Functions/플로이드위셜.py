import sys

INF = int(1e9)

def floyd_warshall(n, edges):
    """
    n: 노드 개수
    edges: (a, b, c) 형태의 간선 리스트 (a -> b 비용 = c)
    return: n+1 x n+1 최단 거리 행렬
    """
    # 그래프 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신으로 가는 비용 = 0
    for a in range(1, n + 1):
        graph[a][a] = 0

    # 간선 정보 입력
    for a, b, c in edges:
        graph[a][b] = min(graph[a][b], c)  # 중복 간선 고려

    # 플로이드 워셜 알고리즘 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    return graph


# 예시 실행
if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    edges = [tuple(map(int, input().split())) for _ in range(m)]

    result = floyd_warshall(n, edges)

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            print(result[a][b] if result[a][b] != INF else "INFINITY", end=" ")
        print()

