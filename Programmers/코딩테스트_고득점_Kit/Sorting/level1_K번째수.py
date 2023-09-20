# https://school.programmers.co.kr/learn/courses/30/lessons/42748


def solution(array, commands):
    answer = []
    for command in commands:
        arr = sorted(array[command[0] - 1 : command[1]])
        answer.append(arr[command[2] - 1])
    return answer
