# https://school.programmers.co.kr/learn/courses/30/lessons/92344
# 그냥 구현방식으로 했더니 효율성을 충족하지 못했다.
# 솔루션을 봤는데, "누적합"을 사용하면 효율성 문제를 해결할 수 있었다.
# https://kimjingo.tistory.com/155


def solution(board, skill):
    answer = 0
    cum_sum = [
        [0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)
    ]  # 누적합 기록 배열

    for type, r1, c1, r2, c2, degree in skill:
        cum_sum[r1][c1] += degree if type == 2 else -degree  # 부호 주의!. 그림 그려서 이해하기
        cum_sum[r1][c2 + 1] += -degree if type == 2 else degree
        cum_sum[r2 + 1][c1] += -degree if type == 2 else degree
        cum_sum[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    # 먼저 행 방향으로 누적합 계산
    for i in range(len(cum_sum) - 1):
        for j in range(len(cum_sum[0]) - 1):
            cum_sum[i][j + 1] += cum_sum[i][j]

    # 열 방향으로 누적합 계산
    for j in range(len(cum_sum[0]) - 1):
        for i in range(len(cum_sum) - 1):
            cum_sum[i + 1][j] += cum_sum[i][j]

    # 기존의 배열과 누적합 배열을 통해 값 계산
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + cum_sum[i][j] > 0:
                answer += 1
    return answer
