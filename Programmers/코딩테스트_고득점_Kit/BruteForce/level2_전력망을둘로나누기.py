# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# https://computer-science-student.tistory.com/654
# 위 풀이를 참고함
# 처음에 아이디어는 떠올랐으나, 구현을 어떻게 해야 할지 감을 못잡아 헤맴
# bfs사용해 그래프 별 노드 개수 세는 부분에 유의
# defaultdict 사용법 유의
# 프로그래머스에서 디버깅 할때는 주석처리해서 하자
# 큐 선언 시에 초기값 지정할 때는 iterable한 자료형이어야 함(리스트 등..)

from collections import defaultdict, deque


def bfs_node_cnt(node_cnt, graph, del_wire):
    # bfs 위해 초기 상태 지정
    connection_cnt = 1  # 연결된 노드의 수
    visited = [False] * (node_cnt + 1)  # 노드 1번부터 시작하는 것 고려
    visited[del_wire[0]] = True  # 시작 노드 방문처리
    queue = deque([del_wire[0]])  # 큐에 시작 노드 넣어둠

    while queue:  # bfs 수행하며 한쪽 영역 그래프의 노드 수 구함
        curr_start_node = queue.popleft()
        for curr_end_node in graph[curr_start_node]:  # 현재 시작점 노드와 연결된 모든 노드에 대해
            if (
                visited[curr_end_node] or curr_end_node == del_wire[1]
            ):  # 이미 방문했거나 연결 끊기는 경우
                continue
            else:  # 방문 안한 경우
                connection_cnt += 1  # 노드 수 추가
                queue.append(curr_end_node)  # 다음 connection 검사 위해 큐에 추가
                visited[curr_end_node] = True  # 방문처리
    return connection_cnt  # 한 쪽 영역 그래프의 총 노드 수 반환


def solution(n, wires):
    answer = float("inf")
    graph = defaultdict(list)
    for start, end in wires:  # 연결정보 기록 위함. 양방향 그래프
        graph[start].append(end)
        graph[end].append(start)

    for wire in wires:
        connection_cnt = bfs_node_cnt(
            n, graph, wire
        )  # 특정 연결 부분 끊어 둘 중 하나 트리의 노드 수 구하는 함수 호출
        answer = min(answer, abs((n - connection_cnt) - connection_cnt))  # 절대값 최소값 반환
    return answer
