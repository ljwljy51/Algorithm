import sys
import heapq
input = sys.stdin.readline

node, edge=map(int, input().split()) #정점 개수, edge 개수
start=int(input()) #시작 정점
INF=int(1e9)
weight=[INF]*(node+1) #가중치 테이블 초기화. 일단 큰 값으로 해둠
graph=[[] for _ in range(node+1)] #그래프 정보 저장 위함

#edge 정보 입력받음
for _ in range(edge):
    node1, node2, w=map(int, input().split()) #정보 입력받음
    graph[node1].append((w, node2)) #목적지 노드와 가중치 정보를 튜플로 해서 그래프에 저장
    
def dijkstra(start):
    heap=[]
    weight[start]=0 #시작 정점에 대한 weight 0으로 초기화
    heapq.heappush(heap, (0, start)) #시작 노드부터 탐색 위함

    while heap: #힙이 빌 때까지
        dist, cur=heapq.heappop(heap) #힙 요소 중 최단 거리 갖는 것 pop
        if weight[cur]<dist: #현재 weight 테이블 정보보다 가중치가 크면 무시
            continue

        #weight 테이블 정보보다 가중치 작으면
        for w, other_node in graph[cur]: #인접 노드 확인
            cost=dist+w #인접 노드로의 가중치 계산
            if cost<weight[other_node]: #계산된 가중치가 기록되어있는 값보다 작으면
                weight[other_node]=cost
                heapq.heappush(heap, (cost, other_node)) #해당 노드에 대한 정보 힙에 삽입

dijkstra(start) 

for i in range(1, node+1):
    print("INF" if weight[i]==INF else weight[i])
    #구해진 결과 출력