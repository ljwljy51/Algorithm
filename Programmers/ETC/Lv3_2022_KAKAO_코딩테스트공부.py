# https://school.programmers.co.kr/learn/courses/30/lessons/118668
# 난 알고력 코딩력 둘 다 부족한듯 ㅋㅋ ㅜ
# 입력 조건이 크지 않다.
# DP?

# 구현 방안이 도저히 생각이 안나서 또 ㅋㅋ 솔루션을 봐버렸다.
# 효율성을 위해 DP를 사용해야 한다고 한다.
# DP문제는 항상 점화식 도출이 가장 어려운 것 같다.. (배열의 각 원소값이 어떤 값을 갖도록 할 것인가를 정의하는 것) -> 문제를 잘 읽자
# https://velog.io/@0_hun/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B3%B5%EB%B6%80-2022-KAKAO-TECH-INTERNSHIP-Level-3-Python


def solution(alp, cop, problems):
    max_alp_req = max(problems, key=lambda x: x[0])[0]  # 목표값. 요구되는 알고력, 코딩력의 최대값
    max_cop_req = max(problems, key=lambda x: x[1])[1]

    dp = [
        [float("inf") for _ in range(max_cop_req + 1)] for _ in range(max_alp_req + 1)
    ]  # dp[i][j]는 알고력 i, 코딩력 j룰 도달할 수 있는 최단시간 값을 가짐

    # dp배열 참조 시 인덱스 오류 방지 위해 alp, cop값 다시 계산(어차피 최대요구값 넘길 필요 x)
    alp = min(alp, max_alp_req)
    cop = min(cop, max_cop_req)

    # dp 배열 초기값 지정 (현재 알고력, 코딩력이 기준이 되도록)
    dp[alp][cop] = 0  # 즉 alp의 알고력, cop의 코딩력을 가질 때까지 0만큼의 시간이 걸린다는 것

    for current_alp in range(alp, max_alp_req + 1):  # 반복문 돌며 dp 배열 채우기
        for current_cop in range(cop, max_cop_req + 1):
            if current_alp < max_alp_req:  # 현재 알고력이 도달해야 하는 알고력보다 작은 경우
                dp[current_alp + 1][current_cop] = min(
                    dp[current_alp + 1][current_cop], dp[current_alp][current_cop] + 1
                )  # 기존에 기록되어있던 최소시간과 비교해 최소값 저장 (알고력 1 높이는 데 1만큼의 시간 소요)

            if current_cop < max_cop_req:  # 현재 코딩력이 ~
                dp[current_alp][current_cop + 1] = min(
                    dp[current_alp][current_cop + 1], dp[current_alp][current_cop] + 1
                )

            # 각 배열값 갱신할 때마다 풀 수 있는 문제들 확인하며 dp배열값 갱신
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if current_alp >= alp_req and current_cop >= cop_req:  # 풀 수 있는 문제
                    new_alp = min(
                        current_alp + alp_rwd, max_alp_req
                    )  # 각 문제를 풀었을때의 알고력, 코딩력 계산. 이때 요구되는 값을 넘지는 않도록 함 (인덱스 오류 방지)
                    new_cop = min(current_cop + cop_rwd, max_cop_req)
                    # 문제 푼 뒤 도달하는 알고력, 코딩력에 대해 dp배열값 갱신
                    dp[new_alp][new_cop] = min(
                        dp[new_alp][new_cop], dp[current_alp][current_cop] + cost
                    )  # 기존 기록된 시간과 각 문제를 풀었을 때 걸리는 최소 시간과 비교해 최소값으로 갱신

    return dp[max_alp_req][max_cop_req]
