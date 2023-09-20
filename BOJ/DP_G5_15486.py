# https://www.acmicpc.net/problem/15486
# 접근 방식에 초점 두기
import sys

input = sys.stdin.readline

n = int(input())  # n+1일에 퇴사

t = [0] * (n + 2)  # 상담에 걸리는 시간
p = [0] * (n + 2)  # 금액
dp = [0] * (n + 2)  # dp값


for i in range(1, n + 1):
    tmp_t, tmp_p = map(int, input().split())
    t[i] = tmp_t
    p[i] = tmp_p  # 값 입력받아 저장

dp[n + 1] = 0  # 첫번쨰 dp값 계산 위해 초기화
for i in range(n, 0, -1):  # 뒤에서부터 접근
    if i + t[i] - 1 > n:  # 만약 상담이 퇴사 날짜 이후에 끝나면
        dp[i] = dp[i + 1]  # 그 다음날에서의 최대값이 현재에서의 최대값이 됨
    else:
        dp[i] = max(
            p[i] + dp[i + t[i]], dp[i + 1]
        )  # i번째 날짜의 상담을 하는 경우와 안하는 경우 고려해 최대값 저장

print(dp[1])  # 첫 번째 날짜에 최대값이 저장되어있음
