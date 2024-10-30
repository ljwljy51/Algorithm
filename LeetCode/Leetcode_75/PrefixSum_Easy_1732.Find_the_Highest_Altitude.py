# 간단한 누적합 구하기
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_al = max_al = 0
        for n in gain:
            cur_al += n
            max_al = max(cur_al, max_al)
        return max_al
