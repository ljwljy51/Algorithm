# https://www.acmicpc.net/problem/11722
# LIS랑 접근 방식은 같음
import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
nums = list(
    map(lambda x: int(x) * -1, input().split())
)  # bisect가 오름차순 기준 정렬본에서 삽입 위치 결정하는 것을 고려

lds = [0]

for num in nums:
    if lds[-1] < num:
        lds.append(num)
    else:
        lds[bisect_left(lds, num)] = num

print(len(lds))
