# https://www.acmicpc.net/problem/11726
# DP
import sys

input = sys.stdin.readline
n = int(input())
dp = [1, 2]  # n=1, n=2에 대한 값 초기화
for i in range(2, n):
    dp.append(dp[i - 2] + dp[i - 1])

print(dp[n - 1] % 10007)
