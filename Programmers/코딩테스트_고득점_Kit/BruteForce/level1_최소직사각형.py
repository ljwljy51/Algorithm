# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# max 함수 다루는 부분에 주목
def solution(sizes):
    max_width = 0

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:  # 더 큰 값을 width로 둠
            tmp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = tmp
        if max_width < sizes[i][0]:
            max_width = sizes[i][0]  # 최대 가로 길이 저장
    print(max_width)
    # 이 시점에서 모든 요소는 가로가 세로보다 긴 형태
    return max_width * (max(sizes, key=lambda x: x[1])[1])  # 세로 길이 중 최대값 찾아 너비 계산해 ㄹ턴
