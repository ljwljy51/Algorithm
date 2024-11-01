# answer배열의 형식을 잘못이해해서 헤맴
class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n + 1):
            answer.append(bin(i).count("1"))  # bin함수를 통해 이진수 변환값을 문자열 형태로 받고, 1의 개수 세기
        return answer
