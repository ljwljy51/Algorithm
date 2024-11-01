# 계단 DP문제
# 재귀 사용 시 TLE 발생..
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        destination = len(cost)
        dp = [0] * destination
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, destination):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[destination - 1], dp[destination - 2])
