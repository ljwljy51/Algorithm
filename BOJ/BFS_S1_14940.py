# https://www.acmicpc.net/problem/14940
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

dir_y = [0, 0, -1, 1]
dir_x = [1, -1, 0, 0]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))  # 시작점 넣어둠

    visited[i][j] = 0  # 방문처리(거리 기록)

    while queue:
        y, x = queue.popleft()

        for idx in range(4):
            new_y, new_x = y + dir_y[idx], x + dir_x[idx]

            # 인덱스 체크
            if 0 <= new_y < n and 0 <= new_x < m and visited[new_y][new_x] == -1:
                if board[new_y][new_x] == 0:  # 갈 수 없는 곳인 경우
                    visited[new_y][new_x] = 0  # 거리 기록
                else:  # 갈 수 있는 경우
                    visited[new_y][new_x] = visited[y][x] + 1  # 기존 거리+1해서 기록
                    queue.append((new_y, new_x))  # 큐에 추가


flag = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:  # 목표지점
            bfs(i, j)
            flag = 1
    if flag == 1:
        break

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:  # 갈 수 없는 곳인 경우. 이 부분 처리 잘못해서 틀렸었음. 문제 잘 읽자
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()
