# 문제는 쉬우나, 제한조건으로 인해 생각했던 알고리즘들이 해당 조건을 충족하지 못함
# 비트연산 사용
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 파이썬 xor연산 -> 비트 같으면 0, 다르면 1 반환
        answer = 0
        for num in nums:
            answer ^= num  # 같은 숫자 나올 경우, xor연산값은 0이 될 것

        return answer
