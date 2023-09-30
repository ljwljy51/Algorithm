# https://school.programmers.co.kr/learn/courses/30/lessons/42885?language=python3
# 구명보트에 최대 두 명만 탈 수 있다는 조건을 제대로 못봐서 헤맸다.
# 투포인터 사용


def solution(people, limit):
    people.sort()  # 정렬
    start, end = 0, len(people) - 1  # 투 포인터 사용 위함

    boat_cnt = 0
    while start <= end:
        boat_cnt += 1
        if people[start] + people[end] <= limit:  # 가장 가벼운 사람과 가장 무거운 사람 먼저 태움
            start += 1
            end -= 1
        else:  # 무거운 사람 한 명만 태움 (그래야 효율적)
            end -= 1

    return boat_cnt
