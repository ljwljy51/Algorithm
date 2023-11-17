# https://school.programmers.co.kr/learn/courses/30/lessons/118669
# 뮨제 조건 잘 이해하기

# 다익스트라 알고리즘 활용
# https://sinclairstudio.tistory.com/231

# in 연산을 사용할 때는 리스트 대신 set 자료형으로 변경하면 훨씬 빠르다 !!!! O(N)->O(1)

from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    intensity = [float("inf")] * (n + 1)  # 출발점에서 각 노드까지의 intensity
    graph = defaultdict(list)  # 그래프 정보 저장 위함
    for start, end, weight in paths:
        graph[start].append((weight, end))  # weight, 도착지점 순으로 저장되도록 함
        graph[end].append((weight, start))

    summits.sort()  # 산봉우리 낮은 것부터 가기 위함
    summits_set = set(summits)  # set에서 in 연산을 사용했을 때 더 빠름

    def get_intensity():
        queue = []  # 우선순위 큐로 사용

        # 모든 출입구에 대한 정보를 큐에 넣어둠
        for gate in gates:
            heapq.heappush(queue, (0, gate))  # weight, 현재 노드
            intensity[gate] = 0  # 출발점->출발점으로의 weight는 0

        while queue:
            weight, current_node = heapq.heappop(queue)  # weight가 작은 것부터 빠져나옴
            if (
                current_node in summits_set or weight > intensity[current_node]
            ):  # 현재 노드가 산봉우리거나 현재 노드에 대한 가중치가 기존에 저장된 가중치 정보보다 큰 경우는 탐색할 필요 없음
                continue

            for next_weight, next_node in graph[
                current_node
            ]:  # 현재 노드와 연결된 노드의 정보를 가져와 처리
                new_intensity = max(
                    weight, next_weight
                )  # 현재 노드의 가중치와 다음 노드의 가중치를 비교해 더 큰 값으로 intensity 정보 갱신 위함
                if (
                    new_intensity < intensity[next_node]
                ):  # 다음 노드에 대한 intensity정보보다 현재 계산된 새로운 intensity가 더 작은 경우에만 정보 갱신
                    intensity[next_node] = new_intensity
                    heapq.heappush(queue, (new_intensity, next_node))  # 큐에 연결정보 넣어둠

        result = [0, float("inf")]
        # 모든 처리가 완료된 경우
        for summit in summits:  # 모든 봉우리에 대해 확인
            if intensity[summit] < result[1]:  # 최소 intensity를 추출하기 위함
                result[0] = summit
                result[1] = intensity[summit]

        return result

    return get_intensity()
