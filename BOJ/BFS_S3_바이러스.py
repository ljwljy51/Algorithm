# https://www.acmicpc.net/problem/2606
import sys
from collections import defaultdict, deque

input = sys.stdin.readline
n_computer = int(input())
n_edge = int(input())
dic = defaultdict(list)

for _ in range(n_edge):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)  # 네트워크 기록

visited = [0 for _ in range(n_computer + 1)]
answer = 0

queue = deque([1])  # 1번 컴퓨터와 연결된 것만 확인 위함
visited[1] = 1
while queue:
    current_node = queue.popleft()
    for next_node in dic[current_node]:
        if not visited[next_node]:
            answer += 1
            queue.append(next_node)
            visited[next_node] = 1


print(answer)  # 1 제외하고 갯수 셈
