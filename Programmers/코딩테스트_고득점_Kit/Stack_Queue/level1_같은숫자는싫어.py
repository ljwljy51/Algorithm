# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = [arr[0]]  # 초기값 지정
    for num in arr[1:]:
        if answer[-1] != num:
            answer.append(num)
        else:
            continue
    return answer
