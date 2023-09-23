# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 시간복잡도를 크게 고려하지 않았음


def check_answer(answers, person):
    cnt = 0
    for i in range(len(answers)):
        if answers[i] == person[i]:
            cnt += 1
    return cnt


# 요소 같은지 확인, (for문 돌면서) 같은만큼 수를 return하는 함수


def solution(answers):
    first_num = [1, 2, 3, 4, 5]  # 각 사람 별 찍는 방식
    second_num = [2, 1, 2, 3, 2, 4, 2, 5]
    third_num = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    first_a = (
        first_num * (len(answers) // len(first_num))
        + first_num[: (len(answers) % len(first_num))]
    )
    second_a = (
        second_num * (len(answers) // len(second_num))
        + second_num[: (len(answers) % len(second_num))]
    )
    third_a = (
        third_num * (len(answers) // len(third_num))
        + third_num[: (len(answers) % len(third_num))]
    )  # 각자의 답안 리스트 생성

    dict_cnt = {}  # 맞은 개수 기록하는 dictionary
    dict_cnt[1] = check_answer(answers, first_a)
    dict_cnt[2] = check_answer(answers, second_a)
    dict_cnt[3] = check_answer(answers, third_a)
    answer = [
        k for k, v in dict_cnt.items() if max(dict_cnt.values()) == v
    ]  # 이렇게 안하고 그냥 max함수 쓰면 최대값 여러 개인 경우 하나만 나옴

    return answer
