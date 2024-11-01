# https://leetcode.com/problems/prime-subtraction-operation/description/
# 소수 판별 알고리즘


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def is_prime(n):  # 소수 판별
            if n == 1:
                return False
            for i in range(2, (int(n ** 0.5) + 1)):
                if n % i == 0:  # 나눠떨어지면 소수 아님
                    return False
            return True

        def find_prime(cur_num, tmp):
            for i in range(tmp, 1, -1):
                if is_prime(i) and cur_num - i != 0:  # 빼는 수가 소수이면서 뺀 결과가 0이 아닐 때
                    return cur_num - i
            return cur_num  # 뺄 수 있는 소수 못 찾았을 경우 원래 수 return

        cur_min = 0  # 현재 기준 최소값
        for i in range(len(nums)):
            if nums[i] <= cur_min:  # 지금까지의 최소값보다 현재 수가 같거나 작으면 false return
                return False

            if i == len(nums) - 1:  # 끝까지 도달한 경우
                return True

            tmp = nums[i] - cur_min - 1  # 현재까지의 최소값을 기준으로 빼야 할 수가 정해짐
            cur_min = find_prime(nums[i], tmp)  # 현재 수에서 가능한 소수 중 최대값을 뺀 값
