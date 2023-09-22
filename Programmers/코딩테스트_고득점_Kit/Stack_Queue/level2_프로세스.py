# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 입력 최대 개수가 100이었기에, 시간복잡도 크게 고려하지 않았음

from collections import deque


def solution(priorities, location):
    queue = deque()
    for i, priority in enumerate(priorities):
        queue.append([i, priority])  # job 별 인덱스 및 우선순위 append

    priority_lst = sorted(priorities, reverse=True)  # 우선순위에 해당하는지 확인하기 위함
    answer = 0
    while queue:
        job = queue.popleft()  # 프로세스 확인
        if job[1] == priority_lst[0]:  # 현재 프로세스의 우선순위가 가장 높으면
            answer += 1  # 프로세스 처리 순서 증가
            del priority_lst[0]  # 우선순위 리스트에서 해당 우선순위 제거
            if job[0] == location:  # 알고싶은 프로세스 번호와 일치하는 경우
                return answer
        else:  # 우선순위가 가장 높지 않은 경우
            queue.append(job)  # 대기열에 다시 append
