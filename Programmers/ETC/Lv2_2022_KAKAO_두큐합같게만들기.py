# 매 번 sum()을 호출해 계산하지 말고 별도의 변수 선언해두기
# 정확도는 맞았으나, 시간초과가 계속 발생했다.
# 큐 자료구조를 사용하고 입력 조건을 고려해 범위를 설정해줬더니 해결됐다.

from collections import deque


def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    first_sum = sum(queue1)
    second_sum = sum(queue2)
    target = (first_sum + second_sum) // 2  # 두 큐의 원소 합이 target과 같아져야 함

    answer = 0
    while first_sum != target:  # 그냥 하드코딩해줬음
        if second_sum > first_sum:
            tmp = queue2.popleft()
            queue1.append(tmp)
            second_sum -= tmp
            first_sum += tmp
            answer += 1
            if tmp > target or answer > 300000:
                return -1
        else:
            tmp = queue1.popleft()
            queue2.append(tmp)
            first_sum -= tmp
            second_sum += tmp
            answer += 1
            if tmp > target or answer > 300000:
                return -1
    return answer
