# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
# string은 "변경 불가능"한 자료구조이므로, 리스트형으로 문자열 요소 조정 후 join함수 활용해 string으로 반환해야 함
# binarysearch


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def get_alphabet(c, is_smaller):  # 다음에 들어가야 할 알파벳을 반환하는 함수
            if c == "a":  # 이전 알파벳과 중복되면 안됨
                return "b" if is_smaller else "c"
            if c == "b":
                return "a" if is_smaller else "c"
            if c == "c":
                return "a" if is_smaller else "b"

        answer = []
        happy_string_cnt = 3 * (2 ** (n - 1))  # 만들 수 있는 happy string 개수

        if happy_string_cnt < k:  # 만들 수 있는 happy string 개수보다 k가 큰 경우
            return "".join(answer)  # 리턴

        st = happy_string_cnt // 3  # 맨 첫 알파벳 결정 기준 (a,b,c)
        # 초기값 지정
        if k <= st:
            answer.append("a")
            start, end = 1, st  # 각 case 별 binary search 기준 설정
        elif k <= st * 2:
            answer.append("b")
            start, end = st + 1, st * 2
        else:
            answer.append("c")  # happy string의 첫 알파벳이 결정됨
            start, end = st * 2 + 1, st * 3

        if n == 1:  # 만들어야 할 string length가 1인 경우
            return "".join(answer)  # 바로 리턴

        while True:
            if start == end:  # 이진탐색 종료 조건
                return "".join(answer)

            mid = (start + end) // 2  # 이진탐색 진행 위함. 절반으로 나눴을 때 왼쪽 값이 mid값이 됨
            if k <= mid:  # 기준보다 k가 왼쪽에 있을 경우
                answer.append(get_alphabet(answer[-1], 1))  # 가능한 알파벳 중 더 작은 알파벳 넣어줌
                end = mid  # 이진탐색 기준 갱신
            else:
                answer.append(get_alphabet(answer[-1], 0))  # 가능한 알파벳 중 더 큰 알파벳 넣어줌
                start = mid + 1
