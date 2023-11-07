# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 밑에서부터 위로 올라가며 최종 root에 도달하고, 그 값을 리턴
# 레벨 3이라 처음에 쫄았는데, 생각보다 쉬웠다.


def solution(triangle):
    depth = len(triangle)  # 삼각형의 총 depth
    for i in range(depth - 2, -1, -1):  # 위로 올라가며 탐색
        for j in range(len(triangle[i])):
            triangle[i][j] += (
                triangle[i + 1][j]
                if triangle[i + 1][j] > triangle[i + 1][j + 1]
                else triangle[i + 1][j + 1]
            )

    return triangle[0][0]
