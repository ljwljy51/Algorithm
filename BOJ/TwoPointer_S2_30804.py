# https://www.acmicpc.net/problem/30804
# 입력길이가 긺-> 효율성 고려 필요
# 앞뒤 빼서 개수 세는 것이므로, 투포인터 사용 필요
# 항상 효율성 고려가 가장 어려운 것 같다.
# set변환해 len()으로 distinct한 값 세려 했으나, 시간초과 발생


from collections import defaultdict as dd
import sys

input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))  # 입력값 받기

fruit_cnt_dict = dd(int)  # 과일 개수 세기 위한 dict
left, right = 0, 0
unique_fruit_cnt = 0
max_length = 0

# 두 포인터 위치를 조정해가며 조건 만족값 찾는 방식
while right < N:
    if fruit_cnt_dict[fruits[right]] == 0:  # 오른쪽 포인터가 가르키는 위치의 과일이 없는 경우
        unique_fruit_cnt += 1
    fruit_cnt_dict[fruits[right]] += 1  # 오른쪽 포인터가 가르키는 위치의 과일 개수 추가

    while unique_fruit_cnt > 2:  # distinct과일 수 2개 초과하는 경우
        fruit_cnt_dict[fruits[left]] -= 1  # 왼쪽 포인터가 가르키는 과일 뺌
        if fruit_cnt_dict[fruits[left]] == 0:  # 해당 종류 과일 없는 경우
            unique_fruit_cnt -= 1
        left += 1  # 왼쪽인덱스 옮김

    max_length = max(max_length, right - left + 1)  # 최대 길이값 저장
    right += 1

print(max_length)
