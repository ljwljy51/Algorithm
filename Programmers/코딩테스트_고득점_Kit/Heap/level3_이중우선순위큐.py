# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 힙은 마지막 요소가 최대값이라는 것을 보장하지 않음. 루트가 최소/최대인 것만 보장

import heapq


def solution(operations):
    answer = []
    heap = []
    for operation in operations:
        command, num = operation.split()
        if command == "I":  # 삽입
            heapq.heappush(heap, int(num))
            continue
        else:  # 최대/최소값 삭제
            try:
                if num == "-1":
                    del heap[0]
                else:  # 파이썬은 최소힙 기준으로 구현됨. 루트가 최소인 것만 보장함
                    heap.remove(max(heap))
            except:  # 오류 방지
                continue
    heap.sort()
    return [0, 0] if len(heap) == 0 else [heap[-1], heap[0]]
