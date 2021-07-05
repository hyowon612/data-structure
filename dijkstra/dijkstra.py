import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

s = 0
n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(s):
    Q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(Q, (0, s))
    dist[s] = 0

    while Q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        d, now = heapq.heappop(Q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if dist[now] < d:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = d + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dist[i[0]]:
                heapq.heappush(Q, (cost, i[0]))
                dist[i[0]] = cost


dijkstra(s)

for i in range(0, n):
    if dist[i] == INF:
        print("inf", end=' ')
    else:
        print(dist[i], end=' ')