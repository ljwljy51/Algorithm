# https://www.acmicpc.net/problem/1405
# DFS 사용
# visited 배열 생성에 주목
# 확률 어떻게 다루는지 확인

import sys

input = sys.stdin.readline

n, e_p, w_p, s_p, n_p = map(int, input().split())  # 값 입력받음
prob = [e_p, w_p, s_p, n_p]  # 확률 배열
result = 0

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 동 서 남 북 순서
# 최대 이동 횟수가 n인 것을 고려해 visited 배열 생성
visited = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]


def dfs(y, x, percent, cnt):
    global result
    if cnt == n:  # cnt==N이면 answer에 확률들 더함
        result += percent  # 확률들 더해줌
        return
    visited[y][x] = 1  # 방문처리
    for i in range(4):
        cur_y = y + directions[i][0]  # 새로운 좌표 계산
        cur_x = x + directions[i][1]
        if 0 <= cur_y < (2 * n + 1) and 0 <= cur_x < (2 * n + 1):  # 인덱스 확인
            if not visited[cur_y][cur_x]:  # 방문하지 않았으면
                # 다음 방향 고려해 dfs 함수 다시 호출
                dfs(cur_y, cur_x, percent * (prob[i] / 100), cnt + 1)
                visited[cur_y][cur_x] = 0  # 방문처리 해제


dfs(n, n, 1, 0)
print(result)
