# https://school.programmers.co.kr/learn/courses/30/lessons/49189
# BFS 사용
# 1번 노드로부터 각 노드까지의 "최단거리" 계산
# count함수 사용법에 유의


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]  # 연결정보 담기 위ㅏㅎㅁ
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)  # 무방향이므로 양쪽에 정보 추가

    visited = [0 for _ in range(n + 1)]
    visited[1] = 1  # 1번 노드에 대해 방문처리

    queue = [1]  # 큐에 넣어둠

    while queue:
        current_node = queue.pop(0)  # 첫 번째 요소 pop
        for end in graph[current_node]:  # 각 연결점에 대해
            if not visited[end]:  # 방문 안했을 경우
                visited[end] = (
                    visited[current_node] + 1
                )  # 현재노드까지의 거리정보+1해서 visited 배열 갱신
                queue.append(end)  # 큐에 해당 노드 넣어둠

    return visited.count(max(visited))  # 가장 멀리 떨어진 노드의 수 리턴
