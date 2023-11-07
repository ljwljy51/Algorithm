# 최대 len(money)//2개의 집만 털 수 있음
# 짝수인 경우 / 홀수인 경우가 갈림
# 예전에 백준에서 풀었던 포도주? 문제랑 비슷한듯
# https://inspirit941.tistory.com/161
# 1번 집을 털 경우: 2번부터 마지막 바로 전 집까지 훔칠 수 있는 돈 계산(마지막 집은 털지 못함)
# 1번 집을 털지 않을 경우: 2번부터 마지막 집까지 훔칠 수 있는 돈 계산


def solution(money):
    dp = [0 for _ in range(len(money))]

    # 1번 집 터는 경우
    dp[0] = money[0]
    dp[1] = dp[0]
    for i in range(2, (len(money) - 1)):  # 마지막 집은 못 텀
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    value = max(dp)  # 첫번째 집 무조건 털었을 때의 최대값 저장해둠
    dp = [0 for _ in range(len(money))]
    # 첫 번째 집 털지 않을 경우
    dp[1] = money[1]
    for i in range(2, len(money)):  # 마지막 집까지 볼 수 있음
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])  # 점화식은 동일하게 적용

    return max(value, max(dp))  # 최대값 리턴
