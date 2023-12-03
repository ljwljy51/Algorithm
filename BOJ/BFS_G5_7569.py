# https://www.acmicpc.net/problem/7569
# 우선 전체적으로 bfs 수행
# 수행 결과 탐색하면서 최대값 구하고 0 있으면 -1 리턴
# 입력을 어떻게 3차원 배열로 저장하는지에 주목

import sys
from collections import deque

input = sys.stdin.readline
queue = deque()

M, N, H = map(int, input().split())

days = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dir_x = [-1, 1, 0, 0, 0, 0]
dir_y = [0, 0, -1, 1, 0, 0]
dir_z = [0, 0, 0, 0, -1, 1]

for k in range(H):
    for i in range(N):
        for j in range(M):
            if box[k][i][j] == 1:  # 익은 토마토가 있는 경우
                # 날짜 수 0으로 해 큐에 넣어둠
                days[k][i][j] = 0
                queue.append((k, i, j))


def bfs():
    while queue:
        z, y, x = queue.popleft()
        for idx in range(6):
            new_z, new_y, new_x = z + dir_z[idx], y + dir_y[idx], x + dir_x[idx]

            if (
                0 <= new_z < H
                and 0 <= new_y < N
                and 0 <= new_x < M
                and days[new_z][new_y][new_x] == -1
                and box[new_z][new_y][new_x] == 0
            ):  # 인덱스 벗어나지 않으면서 아직 방문 안한 경우
                days[new_z][new_y][new_x] = days[z][y][x] + 1
                queue.append((new_z, new_y, new_x))


bfs()

max_day = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            max_day = max_day if max_day > days[k][i][j] else days[k][i][j]

            if days[k][i][j] == -1 and box[k][i][j] == 0:
                print(-1)
                exit(0)

print(max_day)
