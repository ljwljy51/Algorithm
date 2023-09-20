# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 어려웠다.. 로직이 왜 이렇게 되는지 이해해 집중


import heapq


def solution(jobs):
    total_time = 0  # 총 걸린 시간
    current_time, cnt = 0, 0  # 현재 시간, 처리한 job 개수
    start_time = -1  # 이전 작업의 시작 시간
    heap = []

    while cnt < len(jobs):
        for job in jobs:
            if (
                start_time < job[0] <= current_time
            ):  # job의 요청 시간이 이전 작업 시작 시간보다 크면서 현재 시간보다 작거나 같은 작업을 최소 힙에 삽입
                heapq.heappush(heap, [job[1], job[0]])  # 처리 소요 시간 기준으로 정렬되기 위함

        if len(heap) > 0:  # 처리할 작업 있는 경우
            current_job = heapq.heappop(heap)  # 처리할 job pop
            start_time = current_time  # 작업 시작 시간 갱신
            current_time += current_job[0]  # 현재 시간 갱신 (작업 처리에 걸리는 시간 더해줌)
            total_time += current_time - current_job[1]  # 작업 요청~처리 종료까지의 시간 계산
            cnt += 1  # 작업 하나 처리 완료

        else:
            current_time += 1  # 처리할 작업 없는 경우

    return total_time // len(jobs)
