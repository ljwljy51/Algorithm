# https://www.acmicpc.net/problem/1107
# 어려운 문제가 아니었는데도 어떻게 풀어야 할지 감을 못잡았었다.
# 단순 완전탐색

import sys

input = sys.stdin.readline
target = int(input())
n = int(input())  # 고장난 버튼 수
broken_buttons = set(map(int, input().split()))  # 고장난 버튼들 담을 집합

# 현재 채널에서 +, -버튼만 사용해 이동하는 경우
min_cnt = abs(100 - target)  # 현재 번호는 100번

# 9만 누를 수 있는 경우를 고려해 range를 100000으로 잡음
for num in range(1000000):
    num = str(num)  # 문자열로 변환
    for i in range(len(num)):  # 각 자리수 번호마다 확인
        if int(num[i]) in broken_buttons:  # 해당 번호 버튼 고장났을 경우
            break

        # 고장난 숫자 없이 마지막까지 온 경우
        # min_cnt값 업데이트
        if i == len(num) - 1:
            min_cnt = min(min_cnt, abs(int(num) - target) + len(num))

print(min_cnt)
