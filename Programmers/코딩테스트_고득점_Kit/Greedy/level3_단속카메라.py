# https://school.programmers.co.kr/learn/courses/30/lessons/42884?language=python3
# 정렬해 접근하는 방식까지는 생각해냈으나, 자꾸 오답이 출력되어 결국 솔루션 봄
# 생각보다 알고리즘 자체는 매우 간단한 편


def solution(routes):
    routes.sort(key=lambda x: x[1])  # 도착 지점 기준으로 정렬
    cnt_camera = 1
    current_arrival = routes[0][1]  # 초기값 지정
    for start, end in routes[1:]:
        if start > current_arrival:  # 새로운 루트의 시작지점이 현재 도착지점의 뒤에 있는 경우
            cnt_camera += 1  # 카메라 개수 추가
            current_arrival = end  # 도착 지점 갱신
    return cnt_camera
