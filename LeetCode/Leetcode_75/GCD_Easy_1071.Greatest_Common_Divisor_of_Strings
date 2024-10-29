# 최대공약수 (gcd) 알고리즘 기반
# 최대공약수 알고리즘을 쓸 수 있다는 것을 캐치하지 못함
# 두 문자열이 공통된 요소를 갖지 않는 경우 미리 걸러주는 것이 핵심


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        else:
            # 두 문자열의 길이를 기준으로 최대공약수를 구해 return
            return str1[: gcd(len(str1), len(str2))]
