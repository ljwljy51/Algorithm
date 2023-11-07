# https://school.programmers.co.kr/learn/courses/30/lessons/49191
# "정확하게 순위를 매길 수 있는 선수의 수"
# 접근법을 생각해내지 못해 결국 솔루션을 봤다
# https://summa-cum-laude.tistory.com/16
# 플로이드-와샬 알고리즘
# 플로이드-와샬 알고리즘은 "모든"노드로부터 "모든" 다른 노드까지의 최단거리를 구하는 알고리즘
# 거리가 아니라 승패 여부만 저장
# 중간정보를 사용해 각 edge의 정보를 갱신해야 하는 경우, 플로이드 와샬 사용한다고 생각


def solution(n, results):
    board = [[0 for _ in range(n)] for _ in range(n)]  # 승패 기록 저장 위함
    for p1, p2 in results:
        board[p1 - 1][p2 - 1] = 1
        board[p2 - 1][p1 - 1] = -1

    for k in range(n):  # 각 노드를 중간점(경로)으로 가정
        for i in range(n):  # 점수판 순회
            for j in range(n):
                if board[i][j] == 0:  # 승패정보 없는 경우
                    if board[i][k] == 1 and board[k][j] == 1:
                        board[i][j] = 1  # 중간노드와의 관계 고려해 정보 계산
                    elif board[i][k] == -1 and board[k][j] == -1:
                        board[i][j] = -1

    # 각 노드의 점수판에 0이 하나인 경우, 다른 노드들에 대한 승패가 모두 결정됐다는 것
    # 해당 경우의 수를 세면 됨
    answer = 0
    for i in range(n):
        if board[i].count(0) == 1:
            answer += 1
    return answer
