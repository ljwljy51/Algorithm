# 단순한 문제
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)  # 최대 사탕 개수

        result = []

        for candy in candies:
            result.append(True if candy + extraCandies >= max_num else False)

        return result
