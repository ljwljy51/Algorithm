def solution(clothes):
    dic = {}  # 옷 저장할 딕셔너리
    for c in clothes:
        try:
            dic[c[1]].append(c[0])
        except:
            dic[c[1]] = [c[0]]

    answer = 1
    for val in dic.values():
        answer *= len(val) + 1  # 아예 안 입는 경우를 고려해 경우의 수 하나 추가
    return answer - 1  # 아무 것도 안 입는 경우 제외
