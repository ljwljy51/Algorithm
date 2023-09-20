import sys
from collections import deque

input = sys.stdin.readline

n=int(input()) #밭 개수 입력받음
graph=[] #그래프 정보 입력받을 리스트
parents=[_ for _ in range(n+1)] #부모 테이블

for i in range(1, n+1):
    graph.append([int(input()), 0, i]) #새로운 논 팔 때 드는 비용 추가
    #우물 파는 비용을 0번 노드에서 해당 노드로의 가중치로 봄

for i in range(1, n+1):
    cost=list(map(int, input().split()))
    for j in range(1, n+1):
        if i==j:
            continue
        graph.append([cost[j-1], i, j]) #각 노드 간 연결하는 데 드는 비용 추가

d=deque(sorted(graph, key= lambda x:x[0])) #비용 기준으로 정렬해서 덱 생성

def find(node):
    if parents[node]==node:
        return node
    else:
        parents[node]=find(parents[node])
        return parents[node] #부모 node 찾아서 return해줌

def union(node1, node2):
    root1=find(node1)
    root2=find(node2)
    if root1==root2:
        return False
    else:
        parents[root2]=root1 #부모 정보 갱신
        return True

total_cost=0
while d: #덱 빌 때까지. 크루스칼 알고리즘
     cost, node1, node2=d.popleft() #요소 꺼내옴
     if union(node1, node2):
        total_cost+=cost

print(total_cost) #최종 cost 출력





