# 2021카카오채용연계형인턴십
# https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 입력 조건이 단순함
# 단순 조건문 사용해 해결
# 이렇게 해도 되긴 하나, 너무 비효율적


# 그냥 리스트랑 enumerate, replace 등을 사용해 풀었어도 시간초과 안남
# 입력 조건이 한정적일 경우, 해시 사용하기!


# def solution(s):
#     answer = ""
#     while s:
#         if s[0].isdigit():  # 숫자일 경우
#             answer += s[0]
#             s = s[1:]
#             continue
#         else:
#             if s[0] == "z":
#                 answer += "0"
#                 s = s[4:]
#                 continue
#             elif s[0] == "o":
#                 answer += "1"
#                 s = s[3:]
#                 continue
#             elif s[0] == "e":
#                 answer += "8"
#                 s = s[5:]
#                 continue
#             elif s[0] == "n":
#                 answer += "9"
#                 s = s[4:]
#                 continue
#             elif s[0] == "t":
#                 if s[1] == "w":
#                     answer += "2"
#                     s = s[3:]
#                     continue
#                 else:
#                     answer += "3"
#                     s = s[5:]
#                     continue
#             elif s[0] == "f":
#                 if s[1] == "o":
#                     answer += "4"
#                     s = s[4:]
#                     continue
#                 else:
#                     answer += "5"
#                     s = s[4:]
#                     continue
#             elif s[0] == "s":
#                 if s[1] == "i":
#                     answer += "6"
#                     s = s[3:]
#                     continue
#                 else:
#                     answer += "7"
#                     s = s[5:]
#                     continue

#     return int(answer)


def solution(s):
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for word, n in num_dict.items():
        s = s.replace(word, n)

    return int(s)
