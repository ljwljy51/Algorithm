#Minimum Spanning Tree 문제
#Prim 알고리즘 사용
#https://www.acmicpc.net/problem/4386

import sys
import heapq as hq


def prim(graph, root_node, n_node):
    heap = []  # 프림알고리즘 위해 힙 사용
    is_connected = [False]*n_node  # 그래프 포함 여부 체크

    total_distance = 0

    hq.heappush(heap, (0, root_node))  # 초기값 넣어줌 (거리, 시작점)

    while heap:  # 요소 모두 처리될 때까지
        distance, node = hq.heappop(heap)
        if not is_connected[node]:  # 그래프에 포함 x면
            is_connected[node] = True  # 그래프에 포함시킴
            total_distance += distance  # 거리 더해줌

            for i in range(n_node):  # 다른 정점과의 거리 정보 heap에 추가
                if graph[node][i] != 0 and not is_connected[i]:  # 자기 자신이 아니면서 그래프에 포함되어있지 않으면  
                    hq.heappush(heap, (graph[node][i], i))  # 힙에 추가

    return total_distance


input = sys.stdin.readline
n_node = int(input())  # 노드 수 입력받음
node_coord = {}  # 노드 별 좌표 저장 딕셔너리

for i in range(n_node):
    node_coord[i] = tuple(map(float, input().split()))  # 노드 당 좌표 저장

graph = [[0]*(n_node) for _ in range(n_node)]  # 그래프 생성 (거리 정보 담기)

for i in range(n_node):
    for j in range(n_node):
        if graph[i][j] == 0:  # 거리 정보 없으면 거리 계산
            distance = (abs(node_coord[i][0]-node_coord[j][0])
                        ** 2+abs(node_coord[i][1]-node_coord[j][1])**2)**0.5
            graph[i][j] = distance
            graph[j][i] = distance

print(round(prim(graph, 0, n_node), 2))
