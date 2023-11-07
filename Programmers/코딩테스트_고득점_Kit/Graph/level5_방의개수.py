# https://school.programmers.co.kr/learn/courses/30/lessons/49190
# Cycle의 수 세면 될 것 같은데 (이렇게 하면 안됐었음)

# 원점 시작
# "노드가 없는 부분에서 교차하는 경우"에 대한 처리를 어떻게 해야 할지 캐치하지 못함
# v(꼭지점의 개수) - e(변의 개수) + f(면의) 개수 = 2
# 대각선으로 변이 교차하는 경우 오일러 공식의 전제 조건인 평면 그래프가 아닐 수 있으므로 1칸이 아니라 2칸으로 그래프를 늘려 1칸마다 꼭짓점으로 생각
# 평면 그래프란. 평면 상에 그래프를 그렸을 때, 두 변이 꼭짓점 이외에 만나지 않도록 그릴 수 있는 그래프
# f = e - v + 2 에서 바깥 평면은 무시되므로 1을 빼준다


def solution(arrows):
    directions = {
        0: (-1, 0),
        1: (-1, 1),
        2: (0, 1),
        3: (1, 1),
        4: (1, 0),
        5: (1, -1),
        6: (0, -1),
        7: (-1, -1),
    }
    current_location = (0, 0)  # 현재 점의 좌표 위치
    v = set({current_location})  # 중복 방지 위해 집합으로 함. 방문한 정점 정보
    e = set()  # edge정보

    for arrow in arrows:
        for i in range(2):  # 두 칸으로 그래프를 늘려 생각
            next_location = (
                current_location[0] + directions[arrow][0],
                current_location[1] + directions[arrow][1],
            )
            v.add(next_location)  # 정점 정보 추가
            e.add(
                (
                    current_location[0] + next_location[0],
                    current_location[1] + next_location[1],
                )
            )  # edge는 점과 점이 이어진 선. 중복 막기 위해 값을 이렇게 함 (도면 참고해 이해하기)
            current_location = next_location  # 현재 위치정보 갱신

    return len(e) - len(v) + 1  # 오일러 공식 참고
