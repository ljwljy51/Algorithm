# 부분 array 총합 평균 최대값 구하기
# sliding window 알고리즘 사용
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = max_sum = sum(nums[:k])  # 최대 sum값 및 현재 sum값 초기화
        for i in range(len(nums) - k):  # i range 조건 제대로 확인
            cur_sum = cur_sum - nums[i] + nums[i + k]  # 새로 계산 및 값 수정
            max_sum = max(cur_sum, max_sum)
        return max_sum / k
