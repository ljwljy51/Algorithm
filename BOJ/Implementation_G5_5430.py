# https://www.acmicpc.net/problem/5430
# 입력 다루는 부분에 주목
# 결과 출력 시 join함수 활용
# 조건에 따른 예외처리 잘 해주기
# 덱 reverse 함수 사용법 주목

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())  # 테스트케이스 수

for _ in range(T):
    commands = input().strip()  # 명령어 받아옴
    n = int(input())  # 숫자 개수

    if n == 0:  # 입력 숫자 없는 경우:
        input()
        nums_deque = deque()
    else:  # 입력 숫자 주어진 경우
        nums_deque = deque(input().strip()[1:-1].split(","))  # 입력 잘 처리해주기!

    is_reversed = False
    is_error_occurred = False  # 에러 발생 여부 파악 위함
    for command in commands:
        if command == "R":  # 뒤집기 명령인 경우
            is_reversed = not is_reversed
        else:  # "지우기 명령인 경우"
            if len(nums_deque) == 0:  # 덱 비어있는데 D 명령 들어온 경우
                print("error")  # 에러 출력
                is_error_occurred = True
                break  # 반복문 빠져나옴

            if is_reversed:  # 뒤집기 옵션 True인 경우
                nums_deque.pop()  # 뒤에서 요소 제거
            else:  # 뒤집기 옵션 False인 경우:
                nums_deque.popleft()  # 앞에서 요소 제거

    if not is_error_occurred:  # 에러 발생하지 않은 경우
        if is_reversed == True:
            nums_deque.reverse()

        print("[" + ",".join(nums_deque) + "]")
