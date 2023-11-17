import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()  # 오름차순으로 정렬

# 투포인터
left, right = 0, n - 1
min_diff = float("inf")  # 기준

while left < right:
    tmp_diff = nums[left] + nums[right]  # 차이 구해둠
    if abs(tmp_diff) < min_diff:  # 현재 차이보다 더 작으면
        min_diff = abs(tmp_diff)  # 값 갱신
        recent_l, recent_r = left, right  # 인덱스 저장
    if tmp_diff < 0:  # 차이가 음수이면
        left += 1  # 왼쪽 포인터 오른쪽으로 한 칸 이동
    elif tmp_diff > 0:  # 차이가 양수이면
        right -= 1  # 오른쪽 포인터 왼쪽으로 한 칸 이동
    else:  # 차이가 0이면
        break

print(nums[recent_l], nums[recent_r])
