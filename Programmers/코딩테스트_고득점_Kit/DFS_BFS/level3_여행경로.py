# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 기본 아이디어는 생각했으나, "경로가 여러 가지"인 것을 처리하는 부분에서 헤맸음
# "모든 티켓을 다 써야 함"
# 알파벳 순서가 앞서는 경로를 먼저 return해야하므로, dfs 전에 sorting해주면 됐었음
# 혼자 풀었었는데, 테케 1,2번이 계속 틀려서 결국 솔루션 봄..ㅎ

from collections import defaultdict

graph = defaultdict(list)
answer = []


def dfs(start):
    while graph[start]:  # 방문할 수 있는 곳 모두 고려
        dfs(graph[start].pop(0))  # 도착지점 중 알파벳 가장 빠른 것으로 다시 출발점 지정

    if not graph[start]:
        answer.append(start)
        return


def solution(tickets):
    for start, end in tickets:
        graph[start].append(end)  # 연결정보 기록

    for start, end in graph.items():
        graph[start].sort()  # 알파벳 순으로 방문해야 하므로 sorting해줌

    dfs("ICN")
    return answer[::-1]  # 순서 반대로 해서 리턴
