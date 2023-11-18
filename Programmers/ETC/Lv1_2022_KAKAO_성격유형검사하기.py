# https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 해시, 단순구현
# 입력 조건이 까다롭지 않아서 하드코딩해줬는데,
# 인덱스 접근 방식으로 %4 사용해서 하면 좋았을듯


def solution(survey, choices):
    dic_scores = {1: 3, 2: 2, 3: 1, 5: 1, 6: 2, 7: 3}
    user_score = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for i in range(len(survey)):
        if choices[i] < 4:  # 답변이 비동의쪽인 경우
            user_score[survey[i][0]] += dic_scores[choices[i]]
        elif choices[i] > 4:  # 답변이 동의쪽인 경우
            user_score[survey[i][1]] += dic_scores[choices[i]]
        else:  # 모르겠다인 경우
            continue

    answer = ""
    answer += "R" if (user_score["R"] >= user_score["T"]) else "T"
    answer += "C" if (user_score["C"] >= user_score["F"]) else "F"
    answer += "J" if (user_score["J"] >= user_score["M"]) else "M"
    answer += "A" if (user_score["A"] >= user_score["N"]) else "N"

    return answer
