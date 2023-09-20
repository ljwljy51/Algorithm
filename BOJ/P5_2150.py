import sys
from collections import deque
input=sys.stdin.readline

sys.setrecursionlimit(100000) #재귀 깊이로 인한 오류 방지 위함

V, E=map(int, input().split())
graph=[[] for _ in range(V+1)] #그래프 정보 저장 위함

for _ in range(E):
    start, end=map(int, input().split())
    graph[start].append(end) #그래프 정보 저장
    
root=[0 for _ in range(V+1)] #각 노드 별 부모 노드 정보 저장
finished=[0 for _ in range(V+1)] #각 노드 별로 dfs 전부 처리되었는지 여부 저장
cnt=0
s=deque() #스택으로 사용
answer=[] #scc 담을 리스트
def dfs(n):
    global cnt
    cnt+=1 #함수 호출될 때마다 1씩 증가
    root[n]=cnt #초기엔 자기 자신이 root
    s.append(n) #스택에 노드 추가
    parent=root[n] #현재 부모 노드 정보 
    for end in graph[n]: #인접 노드 확인
        if root[end]==0: #아직 인접 노드에 방문 안했으면
            parent=min(parent, dfs(end)) #end 기준으로 dfs 수행해 리턴된 값과 현재 부모 노드 중 작은 값이 parent가 됨
        elif finished[end]==0: #방문은 했으나 아직 dfs 처리 다 안됐으면
            parent=min(parent, root[end]) #dfs 수행중이므로 현재까지 구해진 값으로 갱신
    
    if parent==root[n]: #만약 자신이 부모 노드인 경우
        tmp=[]
        while True:
            current=s[-1] #현재 pop할 요소
            s.pop()
            tmp.append(current)
            finished[current]=1 #처리되었음
            if current==n: #자기 자신 나온 경우
                break
        answer.append(tmp) #scc 리스트에 추가
    return parent #자신의 부모값 반환

for i in range(1,V+1):
    if root[i]==0: #아직 방문 안했을 때만 dfs 함수 호출
        dfs(i)

for i in range(len(answer)):
    answer[i].sort()
    answer[i].append(-1)
answer.sort()

print(len(answer))
for i in range(len(answer)):
    print(*answer[i])