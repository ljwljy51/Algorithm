# 기본적인 문자열 다루기
# 덱 사용
from collections import deque


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        dq1 = deque(list(word1))  # 문자열 -> 리스트 -> 덱 변환
        dq2 = deque(list(word2))

        while (len(dq1) != 0) | (len(dq2) != 0):  # or 혹은 and 조건 사용 시 괄호 잘 넣어주기
            if len(dq1) != 0:
                answer.append(dq1.popleft())
            if len(dq2) != 0:
                answer.append(dq2.popleft())

        return "".join(answer)
