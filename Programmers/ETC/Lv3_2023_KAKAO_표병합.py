# https://school.programmers.co.kr/learn/courses/30/lessons/150366
# PRINT했을때 정답에 값 추가
# 구현문제
# MERGE, UNMERGE 부분에서 헤맸다.
# MERGE, UNMERGE를 다루기 위해 Union Find 알고리즘을 떠올려야 했다.
# 여러 노드가 존재할 때 두 노드를 선택해 두 노드가 같은 그래프 상에 속하는지 판별하는 알고리즘
# https://magentino.tistory.com/69

# 구현 문제지만, 코드 동작 방식이 꽤나 헷갈린다. 잘 이해하자!
# Union Find 알고리즘 작동방식 익히기

parent = [
    [(r, c) for c in range(51)] for r in range(51)
]  # union-find 위함. 초기엔 자신의 부모가 자신이 되도록 함
cells = [["EMPTY"] * 51 for _ in range(51)]  # 각 표 셀이 갖는 값
answer = []


def find(r, c):
    if (r, c) != parent[r][c]:  # 다른 부모 노드가 존재할 경우
        parent_r, parent_c = parent[r][c]
        parent[r][c] = find(parent_r, parent_c)

    # 자신이 루트인 경우
    return parent[r][c]  # 현재 노드 정보 반환


def union(r1, c1, r2, c2):  # 루트노드 값을 기준으로 한다는 가정 존재
    parent[r2][c2] = parent[r1][c1]


def UPDATE(arg):
    if len(arg) == 3:
        r, c, value = int(arg[0]), int(arg[1]), arg[2]
        parent_r, parent_c = find(r, c)  # 부모 노드 찾아 참조 위함
        cells[parent_r][parent_c] = value  # 값 갱신
    else:
        query_value, target_value = arg[0], arg[1]
        for r in range(51):  # 완탐으로 접근. 표 크기가 크지 않기에 가능
            for c in range(51):
                parent_r, parent_c = find(r, c)
                if cells[parent_r][parent_c] == query_value:  # 조건에 따라 값 갱신
                    cells[parent_r][parent_c] = target_value


def MERGE(arg):
    r1, c1, r2, c2 = map(int, arg)
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)  # 루트노드 값을 기준으로 하기 위함

    if (r1, c1) == (r2, c2):
        return
    if cells[r1][c1] != "EMPTY":  # r1,c1위치 셀에 값이 있을 경우
        union(r1, c1, r2, c2)  # r1..값 기준으로 r2..위치 셀 값을 덮어씌움
    else:  # r1,c1 위치 셀에 값이 없을 경우
        union(r2, c2, r1, c1)  # r2..값 기준으로 r1..위치 셀 값을 덮어씌움


def UNMERGE(arg):
    r, c = map(int, arg)  # 입력 셀의 모든 병합을 해제해줘야 함

    parent_r, parent_c = find(r, c)  # 입력 셀의 부모 노드 받아옴
    value = cells[parent_r][parent_c]  # 부모 노드 기준으로 병합 해제 전 셀의 값 가져옴

    merge_lst = list()  # 병합되었던 셀을 담아둘 리스트
    for tmp_r in range(51):
        for tmp_c in range(51):
            parent_tmp_r, parent_tmp_c = find(
                tmp_r, tmp_c
            )  # tmp_r,tmp_c위치의 셀에 대한 부모 노드 정보 가져옴
            if (parent_tmp_r, parent_tmp_c) == (parent_r, parent_c):  # 입력 셀과 병합된 셀인 경우
                merge_lst.append(
                    (tmp_r, tmp_c)
                )  # tmp_r, tmp_c정보를 병합되었던 셀 정보를 담는 리스트에 추가

    for tmp_r, tmp_c in merge_lst:  # 병합되었던 셀 정보 받아옴
        parent[tmp_r][tmp_c] = (tmp_r, tmp_c)  # 병합 해제
        cells[tmp_r][tmp_c] = (
            "EMPTY" if (tmp_r, tmp_c) != (r, c) else value
        )  # 입력 셀의 경우, 병합 해제 전 값을 갖게 하고, 나머지 셀의 경우 EMPTY로 초기화시켜줌


def PRINT(arg):
    r, c = map(int, arg)
    parent_r, parent_c = find(r, c)  # 부모 노드정보 받아옴
    answer.append(cells[parent_r][parent_c])  # 부모노드의 값 가져와 정답에 append


def solution(commands):
    for command in commands:
        cmd, *arg = list(command.split())

        if cmd == "UPDATE":
            UPDATE(arg)
        elif cmd == "MERGE":
            MERGE(arg)
        elif cmd == "UNMERGE":
            UNMERGE(arg)
        else:
            PRINT(arg)

    return answer
