import sys
from collections import deque
input = sys.stdin.readline

n=int(input()) #건물 개수 입력받음
degree=[0 for _ in range(n+1)] #차수 저장
time=[0 for _ in range(n+1)] #건물 짓는데 걸리는 시간
graph=[[] for _ in range(n+1)] #그래프 정보 저장
dp=[0 for _ in range(n+1)] #dp 배열

for i in range(1, n+1):
    tmp=list(map(int, input().split()))[:-1] #마지막 입력 제외하고 저장
    time[i]=tmp[0] #건물 짓는데 걸리는 시간 저장
    for j in tmp[1:]:
        graph[j].append(i) #그래프 연결 정보 저장
        degree[i]+=1 #차수 갱신 

def topology_sort(): #위상정렬 알고리즘 사용
    q=deque()
    for i in range(1,n+1):
        if degree[i]==0: #차수 0인 노드를 큐에 삽입
            q.appendleft(i)
    
    while q: #큐 빌 때까지
        node=q.pop()
        dp[node]+=time[node] #시간 정보 갱신
        for i in graph[node]: #다음에 지어지는 건물들 
            degree[i]-=1 #차수 갱신
            dp[i]=max(dp[i], dp[node]) #지금까지 지어진 건물 짓는데 걸린 시간과 비교해 더 큰 값으로 갱신
            if degree[i]==0: #차수 0이 됐으면 큐에 삽입
                q.appendleft(i)
                
topology_sort()
for i in range(1,n+1):
    print(dp[i])
    

