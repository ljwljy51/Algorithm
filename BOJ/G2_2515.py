# 이분탐색 사용해 시간초과 해결

import sys

input = sys.stdin.readline

N, S = map(int, input().split())  # 그림 개수, s 입력받음
pictures = [list(map(int, input().split())) for _ in range(N)]  # 높이, 가격 정보 저장 리스트
pictures.sort()  # 오름차순으로 정렬

dp = [0]  # DP 배열. 그림 번호에 해당하는 인덱스에 가격 정보 저장되도록 함


def upper_bound(height):  # 이분탐색
    left = 0
    right = N - 1

    while left < right:
        mid = (left + right) // 2
        if pictures[mid][0] <= height:  # 찾는 값이 mid 인덱스 그림의 높이보다 크면
            left = mid + 1  # 왼쪽으로 탐색
        else:  # 찾는 값이 mid 인덱스 그림의 높이보다 작으면
            right = mid  # 오른쪽으로 탐색
    return right  # 조건 만족하는 그림 중에서 가장 높이가 낮은 그림의 인덱스


for i in range(N):
    idx = upper_bound(
        pictures[i][0] - S
    )  # 현재 그림보다 S만큼 높이 낮은 그림보다 높이 높은 그림 중 가장 높이 낮은 그림의 인덱스 리턴받음
    dp.append(
        max(dp[i], dp[idx] + pictures[i][1])
    )  # 기존에 저장되어있던 값과 현재 그림의 가격+방금 구한 인덱스 그림의 총 가격 정보 더한 값을 비교해
    # dp 값 정보 계산. 즉, 가격 계산에 현재 그림을 포함시킴
    # dp 배열의 그림 번호에 해당하는 인덱스에는 그 그림에 대한 총 가격 정보가 저장되어있음(가격의 최대값)

print(dp[N])
