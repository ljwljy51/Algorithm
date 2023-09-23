# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 시간초과 걱정했는데, 시간초과 안나서 당황했다.
def solution(prices):
    answer = []
    for i in range(len(prices) - 1):  # 마지막 요소는 비교 대상 없으므로 포함하지 않음(항상 0)
        current_price = prices[i]  # 현재 기준 가격
        sec = 0  # 지속 시간
        for j in range(i + 1, len(prices)):
            sec += 1  # 바로 다음 시점에 가격 떨어져도 시간 경과한것으로 간주함. 여기서 헷갈렸었음
            if prices[j] < current_price:
                break
        answer.append(sec)
    answer.append(0)  # 마지막 요소 고려
    return answer
