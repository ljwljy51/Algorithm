# https://school.programmers.co.kr/learn/courses/30/lessons/42895
# https://mjmjmj98.tistory.com/106
# DP는 언제 봐도 어려운 것 같다.. 많이 연습하자
# "작은 부분문제들이 반복되는 것"을 이용
# N을 최소로 사용해서 number를 만드는 것이 목표
# 작은 문제도 N의 개수로 정의
# N 사용횟수의 최대값은 8
from collections import defaultdict


def solution(N, number):
    dp = defaultdict(set)  # dp[i]: N을 i번 사용해 만들 수 있는 수들의 집합

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N을 i번 이어붙인 수
        for j in range(1, i):  # n을 몇 번 사용한 결과에 접근하는가에 주목
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        if number in dp[i]:
            return i

    return -1  # N의 사용 횟수가 8을 넘기는 경우
