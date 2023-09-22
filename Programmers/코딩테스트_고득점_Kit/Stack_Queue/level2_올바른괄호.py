# https://school.programmers.co.kr/learn/courses/30/lessons/12909
from collections import deque


def solution(s):
    dq = deque()  # 스택 선언
    for par in s:
        try:
            dq.append(par) if par == "(" else dq.pop()
        except:  # 빈 스택에서 꺼내려고 할 경우
            return False

    return True if len(dq) == 0 else False  # 남아있는 요소가 있으면 false
