# https://school.programmers.co.kr/learn/courses/30/lessons/150367
# 포화이진트리의 개념 제대로 이해하기, 포화이진트리에서 노드 수 구하는 공식에 주목!

# 문제 파악을 제대로 하지 못했다.
# 숫자를 이진수로 변환하는 것 까지는 캐치했으나,
# 이를 "포화이진트리"의 형태가 되도록 해줘야 했다.

# https://chaemi720.tistory.com/310
# "변환한 이진수의 길이를 전체 트리 노드의 수라고 했을 때 포화이진트리가 갖는 최소 노드의 수로 맞춰주라는 뜻" ->이걸 캐치 못함
# 원래 수의 크기는 변하면 안되기 때문에 포화이진트리의 노드의 수에서 현재 길이(노드 수)를 뺀 숫자만큼 더미노드(0)를 앞에 추가
import math


def is_parent_valid(num_bin, parent_node):
    if num_bin == "":
        return True  # 모두 탐색했을 경우 True 반환
    mid = len(num_bin) // 2  # 중간 노드 정보 확인 위함
    current_node = num_bin[mid]  # 현재 노드 정보 확인
    if current_node == "1" and parent_node == "0":  # 자식노드가 1인데 부모 노드가 0인 경우
        return False  # 포화이진트리 아님
    else:  # 계속해서 양쪽 자식방향으로 탐색해나감
        return is_parent_valid(num_bin[:mid], current_node) and is_parent_valid(
            num_bin[mid + 1 :], current_node
        )


def solution(numbers):
    answer = []
    for num in numbers:
        num_bin = bin(num)[2:]  # 각 숫자를 이진수로 변환
        least_node_num = (
            2 ** (int(math.log(len(num_bin), 2)) + 1) - 1
        )  # 포화이진트리에서 노트 수는 2**(높이)-1개의 노드를 가짐
        num_bin = (
            "0" * (least_node_num - len(num_bin)) + num_bin
        )  # 각 숫자에 대해 포화이진트리 형태로 만들어줌

        if len(num_bin) // 2 == "0":  # 루트가 더미인 경우
            answer.append(0)
            continue
        else:
            answer.append(
                1 if is_parent_valid(num_bin, 1) else 0
            )  # 포화이진트리인지 체크 후 맞으면 1, 틀리면 0 append

    return answer
