import heapq


class Solution:
    def sortVowels(self, s: str) -> str:
        def is_vowel(c):  # vowel인지 확인
            if c.lower() in ["a", "e", "i", "o", "u"]:
                return True
            return False

        lst_s = list(s)  #!!문자열은 수정 불가한 자료형. 리스트로 변환해 수정해야 함
        vowel_idxs = []  # vowel 인덱스 저장
        ascii_heap = []  # vowel들의 ascii code 저장할 힙

        for i, c in enumerate(lst_s):
            if is_vowel(c):  # vowel인 경우
                vowel_idxs.append(i)  # 인덱스와
                heapq.heappush(ascii_heap, ord(c))  # 아스키코드 힙 사용해 기억

        for idx in vowel_idxs:
            lst_s[idx] = chr(heapq.heappop(ascii_heap))  # 기억해뒀던 정보 기반으로 문자열 수정
        return "".join(lst_s)  # 리스트를 문자열로 변환해 return
