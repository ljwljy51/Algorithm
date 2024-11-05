# https://www.acmicpc.net/problem/21736

# 기본적인 BFS/DFS 문제
# 난 BFS 사용

from collections import deque
import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
map_info = []  # 맵 정보 담기 위함

answer = 0  # 출력값

N, M = map(int, input().split())  # 맵 크기
visited = [[0] * M for _ in range(N)]  # 방문정보 저장

dq = deque()  # bfs를 위한 덱 생성

for i in range(N):
    map_info.append(list(input().rstrip()))  # 문자열 형태로 입력되는 것 ㄱ도려
    for j in range(M):
        if map_info[i][j] == "I":  # 시작위치인 경우
            dq.append([i, j])
            visited[i][j] = 1

while dq:  # 쿠가 전부 빌 때까지
    cur_y, cur_x = dq.popleft()
    # 네 방향에 대한 탐색 진행
    for i in range(4):
        new_y, new_x = cur_y + dy[i], cur_x + dx[i]  # 새로운 좌표값 계산
        if (
            0 <= new_y < N
            and 0 <= new_x < M
            and map_info[new_y][new_x] != "X"
            and visited[new_y][new_x] == 0
        ):  # 인덱스 초과하지 않으면서 방문 안한 경우
            visited[new_y][new_x] = 1  # 방문처리
            dq.append([new_y, new_x])  # 좌표 추가
            if map_info[new_y][new_x] == "P":  # 사람 만난 경우
                answer += 1  # 만난 사람 수 증가

print("TT" if answer == 0 else answer)
