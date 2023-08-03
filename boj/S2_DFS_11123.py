#https://www.acmicpc.net/problem/11123
#BFS로도 풀 수 있음
#recursion depth 오류 다루는 방법
#방문처리 부분 주목

import sys
sys.setrecursionlimit(10**6)  # 재귀 오류 방지 위함


def dfs(y, x):
    grid[y][x] = "."  # 방문처리
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # 시계방향으로 확인하기 위함
    for i in range(len(directions)):
        next_y = y+directions[i][0]
        next_x = x+directions[i][1]  # 새로운 좌표 계산
        if 0 <= next_y < h and 0 <= next_x < w:  # 인덱스 오류 방지
            if grid[next_y][next_x] == "#":  # 방문하지 않았는데 양 발견되면
                dfs(next_y, next_x)  # dfs 함수 재귀호출


input = sys.stdin.readline
n = int(input())
for _ in range(n):
    h, w = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]  # 그리드 입력받기
    group_cnt = 0

    for i in range(h):  # 그리드 돌면서 확인
        for j in range(w):
            if grid[i][j] == "#":  # 양인 경우
                dfs(i, j)
                group_cnt += 1

    print(group_cnt)  # 정답 출력
