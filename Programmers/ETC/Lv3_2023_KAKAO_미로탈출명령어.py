# https://school.programmers.co.kr/learn/courses/30/lessons/150365
# 사전순대로 봤을 때, d, l, r, u 순으로 빠름
# d..를 최우선으로 두고 나머지를 움직이는 게 좋음
# 최소 경로 먼저 정해두고, 나머지로 왔다갔다
# manhattan distance

# 먼저, manhattan distance 구하고, k에서 distance 뺀 값이 짝수인지 확인, 홀수면 불가능

# BFS로 접근했으나, 그랬더니 시간초과 떴다. BFS는 최대한 많이 접근(?) 넓게 접근하는데, 맵에서 갈 수 없는 구간이 적다 보니 그런듯
# 그리디로 풀 수 있었다!
# https://ddingmin00.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2023-KAKAO-BLIND-RECRUITMENT-%EB%AF%B8%EB%A1%9C-%ED%83%88%EC%B6%9C-%EB%AA%85%EB%A0%B9%EC%96%B4
# 항상 아이디어 생각까지는 그래도 방향에 맞게 하는 것 같은데, 실제로 구현을 제대로 못 하는 것 같다.
# 알고리즘 많이 풀자..

# 남은 거리 계산 위함
def manhattan_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def solution(n, m, x, y, r, c, k):
    if (
        k < manhattan_distance(x, y, r, c)
        or (k - manhattan_distance(x, y, r, c)) % 2 != 0
    ):  # k에서 manhattan distance 뺀 값이 홀수거나, k가 최단거리보다 짧은 경우 불가능
        return "impossible"

    answer = ""
    move_cnt = 0

    # 아래로 일단 최대한 이동
    while x < n and (k - move_cnt) > manhattan_distance(
        x, y, r, c
    ):  # 인덱스 초과하지 않으면서 현재 위치 기준 도착지와의 거리가 최소 거리보다 클 때동안 아래로 이동
        move_cnt += 1
        x += 1  # 현재 위치 행방향으로 1 증가(좌표 x로 지정되어있으니, 헷갈리지 않게 주의)
        answer += "d"

    # 좌측으로 최대한 이동
    while 1 < y and (k - move_cnt) > manhattan_distance(x, y, r, c):
        move_cnt += 1
        y -= 1
        answer += "l"

    # 우좌 반복이동(사전순 고려)
    while (k - move_cnt) > manhattan_distance(x, y, r, c):
        move_cnt += 2
        answer += "rl"  # 좌표변동은 없음

    # 이제 가야 하는 길로 사전순으로 이동
    if x < r:
        answer += "d" * (r - x)  # 최대한 이동
        x = r
    if y > c:
        answer += "l" * (y - c)
        y = c
    if y < c:
        answer += "r" * (c - y)
        y = c
    if x > r:
        answer += "u" * (x - r)
        x = r

    return answer
