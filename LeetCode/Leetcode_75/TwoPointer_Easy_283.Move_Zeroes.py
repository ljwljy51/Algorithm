# 두 개의 포인터를 사용해 조건에 따라 swap해나가는 방식
# 0이 아닌 숫자의 경우 순서 유지 필요
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        anchor = 0  # 투포인터 시작점
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[explorer], nums[anchor] = nums[anchor], nums[explorer]
                anchor += 1  # 다음 swap 위치 계산
