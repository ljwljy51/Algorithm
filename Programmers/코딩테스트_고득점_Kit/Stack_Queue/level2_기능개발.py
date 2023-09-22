# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 뒤에 있는 기능은 먼저 개발되더라도 앞에 있는 기능이 배포될 때 함께 배포된다는 점에 유의
import math


def solution(progresses, speeds):
    answer = []
    day_max = 0  # 최대 걸리는 시간
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])  # 각 progress 당 걸리는 시간 계산

        if day > day_max:
            answer.append(1)
            day_max = day  # 값 갱신
        else:
            answer[-1] = answer[-1] + 1  # 배포할 수 있는 작업 수 추가
    return answer
