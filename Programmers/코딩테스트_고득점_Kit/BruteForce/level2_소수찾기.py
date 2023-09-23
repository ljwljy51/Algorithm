# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 소수 판별 알고리즘에 주목
# string join 함수 자주 사용됨. 잘 기억해두자
import math
from itertools import permutations


def isPrime(num):
    if num <= 1:  # 0이나 1이면
        return False  # 소수 아님
    for i in range(2, int(math.sqrt(num)) + 1):  # 2~num의 제곱근까지 모두 확인
        if num % i == 0:  # i로 나눠떨어지면 소수 아님
            return False

    return True


def solution(numbers):
    num_list = [n for n in numbers]  # 하나씩 분리해서 리스트에 저장
    permutations_set = set()  # 중복 방지 위함
    for i in range(1, len(numbers) + 1):  # 가능한 순열 모두 뽑아냄
        for n in permutations(num_list, i):
            permutations_set.add(int("".join(n)))  # set에 추가해 중복 제거

    answer = 0
    for num in permutations_set:
        answer += 1 if isPrime(num) == True else 0  # 소수 개수 세기

    return answer
