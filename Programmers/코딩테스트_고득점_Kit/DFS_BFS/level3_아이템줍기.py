# 좌표 두 배 해서 5, 5.5, 6..이런식으로 진행될 수 있도록 하기
from collections import deque

map = [[0 for _ in range(102)] for _ in range(102)]
visited = [
    [0 for _ in range(102)] for _ in range(102)
]  # bfs 수행 위함. distance 정보 저장용으로 씀 (메모리 덜 쓰기 위해)
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 시계방향 검사 위함


def bfs(character_x, character_y, item_x, item_y):
    q = deque([(character_x, character_y)]) 

    visited[character_y][character_x] = 1  # 방문정보 및 거리정보 기록

    while len(q) != 0:  # 큐 빌 때 까지
        current_x, current_y = q.popleft()
        for direction in directions:
            new_y, new_x = (
                current_y + direction[0],
                current_x + direction[1],
            )  # 새로운 좌표 계산
            if (
                not visited[new_y][new_x] and map[new_y][new_x] == 1
            ):  # boundary이면서 아직 방문 안했으면
                visited[new_y][new_x] = visited[current_y][current_x] + 1  # 거리정보 갱신
                q.append((new_x, new_y))
                if new_y == item_y and new_x == item_x:  # 도착지점 도달한 경우
                    break

    return (
        visited[item_y][item_x] - 1
    ) // 2  # 좌표 2개했으며, 첫 시작점 distance를 1로 했었기 때문에 값 고려해 반환


def solution(rectangle, characterX, characterY, itemX, itemY):
    for coordinates in rectangle:  # 주어진 좌표 기반으로 맵 생성
        bottom_left_x, bottom_left_y, top_right_x, top_right_y = (
            coordinates[0] * 2,
            coordinates[1] * 2,
            coordinates[2] * 2,
            coordinates[3] * 2,
        )  # 각 좌표 정보 추출 및 저장

        for y in range(bottom_left_y, top_right_y + 1):
            for x in range(bottom_left_x, top_right_x + 1):
                if bottom_left_x < x < top_right_x and bottom_left_y < y < top_right_y:
                    map[y][x] = 2  # 직사각형 내부
                elif map[y][x] != 2:  # 기존 맵에서 직사각형 내부가 아닌 경우
                    map[y][x] = 1  # boundary

    answer = bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2)
    return answer
