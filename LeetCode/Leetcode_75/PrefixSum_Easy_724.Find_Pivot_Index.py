# 양쪽 array 합을 균등하게 나누는 pivot idx 찾기
# pivot값 미포함 계산
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for idx in range(len(nums)):
            right_sum -= nums[idx]
            if left_sum == right_sum:
                return idx
            left_sum += nums[idx]

        return -1
