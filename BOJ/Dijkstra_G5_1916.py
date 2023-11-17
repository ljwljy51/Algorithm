# https://www.acmicpc.net/problem/1916
# 다익스트라 알고리즘
# "하나의 정점"에서 "다른 모든 정점"으로의 최단경로 구하기

import heapq
import sys

input = sys.stdin.readline


def dijkstra(graph, start, num_city):  # 최적경로 탐색
    distances = [float("inf")] * (num_city + 1)  # 무한대 값으로 거리값 초기화
    distances[start] = 0  # 시작점에 대한 거리
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작점 기준 값 큐에 넣어둠

    while queue:
        # 거리 기준 최소값 갖는 것 pop해 거리 및 탐색 대상 노드 받아옴
        cur_dist, cur_dest = heapq.heappop(queue)

        if distances[cur_dest] < cur_dist:  # 기존 최단거리보다 값이 크면 안봐도 됨
            continue

        for new_dest, new_dist in graph[cur_dest]:  # 인접 노드 탐색
            distance = cur_dist + new_dist  # 인접 노드까지의 거리
            if distance < distances[new_dest]:  # 기존 최단거리보다 거리값 작으면 갱신
                distances[new_dest] = distance
                # 다음 인접 노드와의 거리 계산 위함
                heapq.heappush(queue, [distance, new_dest])
    return distances  # 거리 배열 반환


num_city = int(input())
num_bus = int(input())

graph = [[] for _ in range(num_city + 1)]  # 그래프 생성

for _ in range(num_bus):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))  # 그래프 정보 저장
start, end = map(int, input().split())  # 출발 도시 및 도착 도시

distances = dijkstra(graph, start, num_city)
print(distances[end])
