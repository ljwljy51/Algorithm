from collections import deque
from itertools import combinations
import sys
input=sys.stdin.readline

check=[[-1,0], [0,1], [1,0], [0,-1]] #시계방향 체크 위함

N,M=map(int, input().split())
original_map=[list(map(int, input().split())) for _ in range(N)]
position=[] #바이러스 놓을 수 있는 위치
answer=float("inf") #최솟값 찾는 것이 목적이므로 초기값 inf로 설정

def bfs(virus_pos):
    d=deque(virus_pos)
    visited=[[-1 for _ in range(N)] for _ in range(N)] #방문 여부 배열
    sec=0 #최소 시간 확인 위함
    for y, x in d:
        visited[y][x]=0 #처음에 바이러스 놓을 곳들
    while d: #덱 빌 때까지
        old_y,old_x=d.popleft()
        for i in range(4): #사방으로 체크
            y=old_y+check[i][0]
            x=old_x+check[i][1]
            if 0<=y<N and 0<=x<N:#인덱스 범위 만족하면
                if visited[y][x]==-1 and original_map[y][x]!=1: #방문하지 않았으며 벽이 없으면
                    d.append((y,x)) #덱에 추가
                    visited[y][x]=visited[old_y][old_x]+1 #방문 정보 갱신
                    sec=visited[old_y][old_x]+1 
                
    #bfs 수행 완료
    #빈 칸 있는지 확인
    for i in range(N):
        for j in range(N):
            if visited[i][j]==-1 and original_map[i][j]!=1:#방문 안했으면서 벽이 아니면
                return float("inf")
    return sec #빈 칸 없으면 시간 리턴

for i in range(N):
    for j in range(N):
        if original_map[i][j]==2: #바이러스 놓을 수 있는 곳
            position.append((i,j))

for virus_pos in combinations(position, M):
    answer=min(bfs(virus_pos), answer) #최소값 찾음
    
print(answer if answer!=float("inf") else -1)