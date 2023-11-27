# https://school.programmers.co.kr/learn/courses/30/lessons/92345
# 보드 크기가 작음, 플레이어는 항상 두 명
# 완전탐색?
# DFS, 총 이동 횟수 구해 저장해두고 최소값 리턴하는 방식?
# "항상 A가 먼저 시작"


# 역시 솔루션 봤다..^^
# 승리할 사람 입장에서는 최대한 짧은 턴 안에 승리하는 것이, 지는 사람 입장에서는 최대한 길게 끄는 게 최선의 플레이
# 재귀, 백트래킹,  minmax 알고리즘
# https://blog.encrypted.gg/1032
# minmax tree: 최악의 경우 발생가능한 손실을 최소화 한다는 규칙
# 재귀, 백트래킹 너무 어렵다....
# 솔루션 봤는데도 이해가 잘 되진않는다. 백트래킹 문제 익숙해져야 할듯


dx = [0, 0, -1, 1]  # 좌우 이동
dy = [-1, 1, 0, 0]  # 상하 이동
n, m = 0, 0  # 보드 크기 구하기 위함


def index_check(x, y):  # 보드 밖으로 벗어나는지 체크 위함
    return 0 <= y < n and 0 <= x < m


visited = [[0 for _ in range(5)] for _ in range(5)]  # 최대 보드 크기는 5
blocked = [[0 for _ in range(5)] for _ in range(5)]  # 블록 존재 여부

# 현재 상태에서 둘 다 최적의 플레이를 할 때 두 캐릭터가 움직힌 횟수의 총합 반환
# 반환값이 짝수인 경우, 패배. 홀수인 경우, 승리
# cur_x, cur_y는 현재 플레이어의 좌표, op_x, op_y는 상대 플레이어의 좌표


def solve(cur_y, cur_x, op_y, op_x):
    global visited, blocked
    if visited[cur_y][cur_x]:
        return 0  # 현재 밟고있는 곳의 발판이 이미 없어진 경우, 남은 이동 횟수는 0

    ret = 0  # 현재 호출된 함수에서 반환할 값

    # 네 방향으로 확인
    for dir in range(4):
        next_x = cur_x + dx[dir]
        next_y = cur_y + dy[dir]  # 다음 좌표 계산
        if (
            not index_check(next_x, next_y)
            or visited[next_y][next_x]
            or not blocked[next_y][next_x]
        ):  # 다음 위치에 대해 인덱스 벗어나거나 갈 수 없는 경우 진행하지 않음
            continue
        visited[cur_y][cur_x] = 1  # 다음 진행이 가능한 경우 현재 위치에 대해 방문처리

        # 플레이어를 다음 방향으로 이동시켰을 때 턴 수 계산
        # 인자 순서 잘 맞춰주는 것에 주의 (상대 입장과 바꿔야 함)
        # 이때, 다음 턴에서의 좌표값(새로 계산된 좌표)을 전달해야 함
        val = solve(op_y, op_x, next_y, next_x) + 1  # 다음 좌표로 이동 후 남은 이동 횟수

        # 백트래킹
        # 방문표시 해제
        visited[cur_y][cur_x] = 0

        # 반환 값이 짝수이다 = 앞으로 짝수번 이동을 더 한다 = 나 상대 나 상대 ... 나 상대 이렇게 상대가 마지막으로 움직인 후 끝난다 = 내가 진다
        # 현재 저장된 턴은 패배인데 새로 계산된 턴은 승리인 경우
        if ret % 2 == 0 and val % 2 == 1:
            ret = val  # 턴 수 바로 갱신
        # 현재 저장된 턴과 새로 계산된 턴이 모두 패배인 경우
        elif ret % 2 == 0 and val % 2 == 0:
            ret = max(ret, val)  # 최대한 오래 끄는 턴 선택
        # 현재 저장된 턴과 새로 계산된 턴 모두 승리인 경우
        elif ret % 2 == 1 and val % 2 == 1:
            ret = min(ret, val)  # 최대한 빨리 승리하는 턴 선택

    return ret  # 턴 수 반환


def solution(board, aloc, bloc):
    global n, m
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            blocked[i][j] = board[i][j]  # 발판 상태 저장
    return solve(aloc[0], aloc[1], bloc[0], bloc[1])
