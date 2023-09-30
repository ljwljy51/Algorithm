# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# Combination 활용 방안 생각했으나, 시간초과문제로 인해 또 솔루션 봐버림 ㅋㅋ ㅜㅜ...
# 스택 자료구조 활용
# 맨 앞 수를 최대한 크게 유지하되, k만큼의 길이가 되어야 함에 유의
def solution(number, k):
    stack = []
    for n in number:
        while (
            stack and stack[-1] < n and k > 0
        ):  # 스택에 요소가 있고, 머자먹 요소가 현재 숫자보다 작으면서 k만큼의 수를 빼지 않았을 때
            stack.pop()  # 스택에 있던 수 하나 제거
            k -= 1  # 뺴야 할 수의 개수 차감
        stack.append(n)  # 현재 수 append

    return "".join(stack[: len(stack) - k])  # string 슬라이싱 이용
