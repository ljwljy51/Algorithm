from collections import deque

def solution(maps):
    map_check = [[-1, 0] , [0, 1], [1, 0], [0, -1]] #시계방향으로 길이 있는지 체크 위함
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)] #방문 여부 저장 위함
    distance = [[0 for _ in range(m)] for _ in range(n)] #거리 저장 배열
    
    d = deque()
    d.appendleft((0,0)) #시작점을 초기값으로 넣어줌
    visited[0][0] = 1 #시작점의 방문 여부 및 거리 정보 초기화
    distance[0][0] = 1 
    #bfs
    while (len(d) != 0): #큐가 빌 때까지
        old_y, old_x = d.pop() #좌표 하나 뽑아옴
        for i in range(4): #네 방향 체크
            new_x = old_x + map_check[i][1] #새로운 좌표값 계산
            new_y = old_y + map_check[i][0] 
            if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1: #인덱스 범위 체크
                if maps[new_y][new_x] == 1 and visited[new_y][new_x] == 0: #갈 수 있으면서 방문 안했으면
                    d.appendleft((new_y, new_x)) #큐에 넣어줌
                    visited[new_y][new_x] = 1 #방문 처리 및 거리 갱신
                    distance[new_y][new_x] = distance[old_y][old_x] + 1
                    if new_y == n - 1 and new_x == m - 1: #도착지점 도착했으면 break
                        break
    
    #도착지점에 도착한 경우에만 값 리턴
    return distance[n - 1][m - 1] if visited[n - 1][m - 1] == 1 else -1