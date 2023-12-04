# https://ji-gwang.tistory.com/249
# 문제 자체는 어렵지 않은데, 규칙성을 기반으로 식을 도출해내는 과정이 어려웠다.
# 솔루션 봄^^..

import sys

input = sys.stdin.readline

T = int(input())


def calculate(M, N, x, y):
    # x값을 기준으로 탐색
    num = x
    while num <= M * N:  # M*N을 초과할 수는 없음
        if (num - x) % M == 0 and (num - y) % N == 0:  # 두 조건 모두 만족하는 경우
            return num
        # x 기준 탐색이므로, 현재 num에 M값을 더해줌으로써 다음 탐색 진행
        num += M

    # 전부 확인했는데 마땅한 값 못 찾은 경우
    return -1


for _ in range(T):
    M, N, x, y = map(int, input().split())

    print(calculate(M, N, x, y))
