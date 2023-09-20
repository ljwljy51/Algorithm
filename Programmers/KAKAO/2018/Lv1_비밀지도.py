# https://school.programmers.co.kr/learn/courses/30/lessons/17681
# 연산 및 함수 적용 순서 유의
# 비트연산 사용


def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        result.append(
            format(arr1[i] | arr2[i], "b").zfill(n).replace("1", "#").replace("0", " ")
        )  # 두 맵 각 위치 숫자의 and 연산 결과를 binary로 변환 후, 자리수 채워 append
    return result
