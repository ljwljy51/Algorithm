# https://school.programmers.co.kr/learn/courses/30/lessons/150369
# 가장 먼 곳에 대한 배달 정보부터 확인해야 함
# 배달 정보 활용해 몇 개의 택배 실어갈건지 / 몇 개씩 수거해올건지 정해야 함
# 그런데 구현 방안 생각이 안나서 또 솔루션 봄 ㅋㅋ...
# https://oh2279.tistory.com/147


def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]  # 가장 먼 곳의 배달 정보부터 탐색하기 위함
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]

        while have_to_deli > 0 or have_to_pick > 0:  # 배달해야하거나 수거해야 할 박스가 하나 이상 있는 경우
            have_to_deli -= cap
            have_to_pick -= cap  # 각 위치마다 트럭 용량 고려해 택배 배달하고 수거해옴
            answer += (n - i) * 2  # 왕복 고려해 거리를 두 배 해서 더해줌

    return answer
