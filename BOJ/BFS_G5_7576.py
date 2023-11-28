# https://www.acmicpc.net/problem/7576

# 우선 전체적으로 bfs 수행
# 수행 결과 탐색하면서 최대값 구하고 0 있으면 -1 리턴

import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

M, N = map(int, input().split())

days = [[-1 for _ in range(M)] for _ in range(N)]
box = [list(map(int, input().split())) for _ in range(N)]
dir_y = [0, 0, -1, 1]
dir_x = [-1, 1, 0, 0]

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:  # 익은 토마토가 있는 경우
            # 날짜 수 0으로 해 큐에 넣어둠
            days[i][j] = 0
            queue.append((i, j))


def bfs():
    while queue:
        y, x = queue.popleft()
        for idx in range(4):
            new_y, new_x = y + dir_y[idx], x + dir_x[idx]

            if (
                0 <= new_y < N
                and 0 <= new_x < M
                and days[new_y][new_x] == -1
                and box[new_y][new_x] != -1
            ):  # 인덱스 벗어나지 않으면서 아직 방문 안한 경우
                days[new_y][new_x] = days[y][x] + 1
                queue.append((new_y, new_x))


bfs()

max_day = 0
for i in range(N):
    for j in range(M):
        max_day = max_day if max_day > days[i][j] else days[i][j]

        if days[i][j] == -1 and box[i][j] == 0:
            max_day = -1

        if max_day == -1:
            break
    if max_day == -1:
        break

print(max_day)
