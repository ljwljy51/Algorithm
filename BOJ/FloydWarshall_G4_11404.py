# https://www.acmicpc.net/problem/11404
# 플로이드 와샬 알고리즘
# "모든 정점"에서 "다른 모든 정점"으로의 최단경로 구하기

import sys

input = sys.stdin.readline


def floyd_warshall():
    distances = [
        [float("inf") for _ in range(num_city + 1)] for _ in range(num_city + 1)
    ]  # 최단경로 담을 배열
    for _ in range(num_bus):
        start, end, weight = map(int, input().split())
        distances[start][end] = min(weight, distances[start][end])

    for mid in range(1, num_city + 1):  # 거치는 노드
        for start in range(1, num_city + 1):  # 시작 노드
            for end in range(1, num_city + 1):  # 도착 노드
                if start == end:
                    distances[start][end] = 0
                else:  # 만약 중간 노드 거쳤을 때 거리가 더 짧으면 거리값 갱신
                    distances[start][end] = min(
                        distances[start][end],
                        distances[start][mid] + distances[mid][end],
                    )

    return distances


num_city = int(input())
num_bus = int(input())

distances = floyd_warshall()

for i in range(1, num_city + 1):
    for j in range(1, num_city + 1):
        if distances[i][j] == float("inf"):
            print(0, end=" ")
        else:
            print(distances[i][j], end=" ")
    print()
