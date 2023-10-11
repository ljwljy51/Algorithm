# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# "최소" 단계를 찾는 것이므로 한 바퀴 돌 때마다 글자 수 하나 다른 것 words에서 제거해주는 게 핵심
from collections import deque


def solution(begin, target, words):
    d = deque([begin])  # 초기값 넣어줌
    cnt = 0  # 몇 바퀴 돌았는지 확인 위함
    while len(d) != 0:  # 덱이 빌 때까지
        cnt += 1
        for _ in range(len(d)):
            begin = d.pop()  # 시작 단어 추출
            for word in words:
                diff_cnt = 0
                for i in range(len(begin)):  # 글자 다른 개수 확인
                    if begin[i] != word[i]:
                        diff_cnt += 1

                if diff_cnt == 1:  # 다른 글자 수가 1개인 경우
                    d.appendleft(word)  # 그 단어를 덱에 넣어둠
                    words.remove(word)  # 단어 리스트에서 해당 단어 삭제

        if target in d:  # target과 같은지확인
            return cnt

    return 0
