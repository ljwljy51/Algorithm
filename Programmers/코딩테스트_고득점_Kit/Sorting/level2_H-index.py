# https://school.programmers.co.kr/learn/courses/30/lessons/42747


# h번 이상 인용된 논문을 h편이상 가지고 있다 -> h-index
def solution(citations):
    citations.sort(reverse=True)  # 인용 수 큰 것부터 검사 위해 내림차순으로 정렬

    for idx, num in enumerate(citations):
        if idx >= num:  # 현재 논문의 인용 수가 현재 논문의 인용수보다 많은 인용 수를 갖는 논문 수 이하일 때 리턴
            return idx

    return len(citations)
