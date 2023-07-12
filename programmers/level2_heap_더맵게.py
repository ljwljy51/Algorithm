import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)  # 최소힙

    while scoville[0] < K:
        if len(scoville) == 1:  # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            return -1
        min_1 = heapq.heappop(scoville)  # 가장 안 매운 음식
        min_2 = heapq.heappop(scoville) * 2  # 두 번째로 안 매운 음식
        heapq.heappush(scoville, min_1 + min_2)  # 섞어서 push
        answer += 1  # 섞은 횟수

    return answer
