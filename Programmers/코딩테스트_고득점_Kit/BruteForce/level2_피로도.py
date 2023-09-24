# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 입력 조건이 크지 않아서 순열 돌려도 되는듯

from itertools import permutations


def solution(k, dungeons):
    max_cnt = 0  # 최대 탐험 가능 던전 수
    for p in permutations(dungeons, len(dungeons)):
        cnt = 0  # 임시 값
        curr_k = k  # 임시 값
        for standard, cost in p:  # 최소 필요 피로도, 소모 피로도
            if curr_k >= standard:  # 기존 충족할 경우
                cnt += 1
                curr_k -= cost
        max_cnt = cnt if cnt > max_cnt else max_cnt  # 최대값 반환 위함
    return max_cnt
