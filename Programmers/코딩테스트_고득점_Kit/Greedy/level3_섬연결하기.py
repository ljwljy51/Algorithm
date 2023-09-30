# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# MST 찾는 문제
# 크루스칼 알고리즘 사용
# union_parent 함수 부분 이해 제대로 하기

parent = []


def find_parent(node):
    if parent[node] != node:  # 자기 자신이 노드가 아닌경우.
        parent[node] = find_parent(parent[node])  # 타고 올라가서 부모 찾음
    return parent[node]


def union_parent(start, end):
    start = find_parent(start)
    end = find_parent(end)  # 각 노드의 부모 노드 찾기
    if start < end:  # 부모 노드 번호에 따라 부모 노드 정보 갱신
        parent[end] = start
    else:
        parent[start] = end


def solution(n, costs):
    total_cost = 0
    global parent
    parent = [_ for _ in range(n)]  # 부모 노드 배열 초기화. 전역변수. 자신의 부모는 자신

    costs.sort(key=lambda x: x[2])  # cost 값 기준으로 정렬
    for i in range(len(costs)):  # edge 하나씩 확인하며 union find
        start, end, cost = costs[i][0], costs[i][1], costs[i][2]
        if find_parent(start) != find_parent(end):  # 두 노드 간 부모가 다르면
            union_parent(start, end)  # 두 노드 속한 그래프 부모 통합
            total_cost += cost  # 그래프에 해당 edge 포함
    return total_cost
