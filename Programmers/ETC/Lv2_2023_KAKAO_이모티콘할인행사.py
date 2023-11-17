# https://school.programmers.co.kr/learn/courses/30/lessons/150368
# 완탐?
# 이모티콘 각각에 대한 할인율 적용 결과 미리 계산
# 역시나 아이디어는 맞았으나 구현을 어떻게 해야할지 감을 못잡았다
# 문제 많이 풀면서 익숙해져야 할듯
# https://kcw0360.tistory.com/16

from itertools import product


def solution(users, emoticons):
    answer = []
    sales = [10, 20, 30, 40]
    for case in product(sales, repeat=len(emoticons)):  # 각 이모티콘에 대한 모든 가능한 할인율의 조합을 뽑아옴
        result = [0, 0]  # 이모티콘 플러스 가입자 수, 이모티콘 구매 총액
        for user in users:
            temp_cost = 0  # 사용자의 이모티콘 구입 지불 비용
            for idx, sale in enumerate(case):  # 각 조합마다의 인덱스와 할인율 받아옴
                if sale >= user[0]:  # 이모티콘 할인율이 유저가 원하는 할인율 이상인 경우
                    temp_cost += emoticons[idx] * (1 - (sale / 100))

            if temp_cost >= user[1]:  # 계산된 값이 예산 초과인 경우 이모티콘 플러스 가입
                result[0] += 1
            else:
                result[1] += temp_cost  # 이모티콘 플러스 가입하지 않는 경우 이모티콘 구입 액 추가
        answer.append(result)  # 각 할인율 경우의 수마다 결과 추가

    answer.sort(key=lambda x: (x[0], x[1]), reverse=True)  # 가입자 수 많은 순서대로 리턴
    return answer[0]
