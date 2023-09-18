from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    d = deque()
    for i in range(n):
        if not visited[i]: #방문 안한 노드가 있으면
            answer += 1 #네트워크 하나 추가
            visited[i] = 1 #방문처리
            d.appendleft(i) #덱에 넣어둠
        while (len(d) != 0): #덱이 빌 때까지 반복
            tmp = d.popleft() #덱을 스택으로 사용. bfs
            for j in range(n):
                if computers[tmp][j] == 1 and not visited[j]: #연결 되어있고 방문 안했으면
                    visited[j] = 1 #방문 처리
                    d.appendleft(j)
    
    return answer