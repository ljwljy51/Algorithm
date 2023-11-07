# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# "최단경로"의 "개수"를 어떻게 구하는가를 캐치하지 못했다.
# 진짜진짜 기본적인 DP문제였다. 알고리즘 꾸준히 풀자..^^.....
# 문제의 좌표가 일반 좌표계와 다르게 구성되어있다는 점에 주의


def solution(m, n, puddles):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]  # 맵 초기화
    dp[1][1] = 1  # 시작 위치

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue  # 시작점인 경우
            if [j, i] in puddles:  # 웅덩이 있는 경우 값은 0
                dp[i][j] = 0
            else:
                dp[i][j] = (
                    dp[i - 1][j] + dp[i][j - 1]
                ) % 1000000007  # 현재 칸은 왼쪽, 위쪽 칸의 합산으로 이뤄짐
    return dp[n][m]
