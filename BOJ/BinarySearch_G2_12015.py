# https://www.acmicpc.net/problem/12015

import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

lis = [0]

for num in nums:
    if lis[-1] < num:  # 마지막 원소보다 지금 수가 크면 그냥 append
        lis.append(num)
    else:  # 리스트에서 오름차순 기준 들어갈 수 있는 위치의 인덱스 받아와 값 대체
        lis[bisect_left(lis, num)] = num
    print(lis)

print(len(lis) - 1)
