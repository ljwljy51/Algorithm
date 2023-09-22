# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 문제 잘못 이해해서 겁나 헤맴..문제 자체는 안어려운데
# https://jyeonnyang2.tistory.com/202의 풀이를 참고함


def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length  # 다리 길이만큼의 배열 생성. 트럭 있으면 무게 넣고, 없으면 0
    cnt = 0  # 총 걸린 시간
    current_weight = 0  # 현재 다리 위 트럭 무게
    while bridge:  # 다리 위에 뭔가 있는 동안
        cnt += 1
        current_weight -= bridge.pop(0)
        if truck_weights:  # 아직 건너지 않은 트럭 있으면
            if current_weight + truck_weights[0] <= weight:  # 건널 수 있는 무게 초과하지 않으면
                current_weight += truck_weights[0]  # 다리 위 무게 정보 갱신
                bridge.append(truck_weights.pop(0))  # 다리에 트럭 넣음
            else:  # 무게 초과하는 경우
                bridge.append(0)  # 무게 0으로 해서 다리 공간 확보 위함
    return cnt
