# 효율성 고려 필요
# 덱 사용

from collections import deque


class Solution:
    def reverseVowels(self, s: str) -> str:
        dq_vowels = deque()  # 모음 저장을 위한 덱
        dq_idxs = deque()  # 인덱스 저장을 위한 덱

        vowel_dict = {
            "A": True,
            "E": True,
            "I": True,
            "O": True,
            "U": True,
            "a": True,
            "e": True,
            "i": True,
            "o": True,
            "u": True,
        }  # 딕셔너리 사용해 검색 용이하도록 함
        s = list(s)
        for i, ch in enumerate(s):
            try:
                vowel_dict[ch]  # 모음 발견한 경우
                dq_vowels.append(ch)  # 해당 모음 및 인덱스를 튜플 형태로 저장
                dq_idxs.append(i)
            except:
                continue

        print(dq_vowels)
        # 덱 요소 뽑아가며 문자열 편집. reverse해야하므로 pop 순서 주의
        while len(dq_vowels) != 0:
            i = dq_idxs.popleft()
            ch = dq_vowels.pop()
            s[i] = ch

        return "".join(s)  # join해 return
