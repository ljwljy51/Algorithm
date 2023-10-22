# https://velog.io/@hyg8702/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8D%BC%EC%A6%90-%EC%A1%B0%EA%B0%81-%EC%B1%84%EC%9A%B0%EA%B8%B0-python%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 어떻게 구현해야할지 정말 감이 하나도 안와서 솔루션 봤다
# 근데 솔루션 봤는데도 감이 잘 안온다
# 단순구현문제가 오히려 제일 까다로운듯


def solution(game_board, table):
    # gameboard의 빈칸, table의 블럭을 찾는 함수
    def finding(arr, num):
        # return할 블럭 및 빈칸들이 있는 배열
        return_lst = []
        visited = [[0 for i in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                # 현재 찾는 것(블럭 or 빈칸)과 같고 방문하지 않았으면 BFS수행
                if arr[i][j] == num and not visited[i][j]:
                    Q = [[i, j]]  # 큐에 넣어둠
                    visited[i][j] = 1  # 방문처리
                    k = 0
                    while k < len(Q):  # 큐에 있는 요소동안 반복(큐 길이 변하는 것에 영향 안받도록 함)
                        r, c = Q[k]  # 기준이 되는 row, col 정보 추출
                        for d in range(4):  # 네 방향으로 탐색
                            nr, nc = (
                                r + directions[d][0],
                                c + directions[d][1],
                            )  # 새로운 row, col 계산
                            if 0 <= nr < n and 0 <= nc < n:  # 인덱스 범위 확인
                                if (
                                    arr[nr][nc] == num and not visited[nr][nc]
                                ):  # 현재 찾는 것(블럭 or 빈칸)과 같고 방문하지 않았으면 BFS수행
                                    Q.append([nr, nc])  # 큐에 요소 추가
                                    visited[nr][nc] = 1  # 방문정보 갱신
                        k += 1  # 기존 큐에 있던 요소 중 처리 개수 파악 위함
                    return_lst.append(Q)  # 지금까지 찾은 요소들 추가
        return return_lst

    # block 위치 인덱스를 1개의 문자열로 이어 반환
    def hashing(group):
        # 해당 도형 위치의 가장 왼쪽 모서리 (좌상단)
        min_r, min_c = 50, 50
        for r, c in group:
            min_r = min(min_r, r)
            min_c = min(min_c, c)

        # 도형 기존 좌표를 좌상단 제일 구석에 넣었을 때의 좌표로 변환
        for i in range(len(group)):
            group[i][0] -= min_r
            group[i][1] -= min_c

        # 오름차순으로 정렬 (첫 번째 기준은 행, 두 번째 기준은 열)
        group.sort()

        # 문자열로 바꿔 리턴
        return_lst = []
        for r, c in group:
            return_lst.append(str(r))
            return_lst.append(str(c))
        return "".join(return_lst)

    # 빈칸의 모양 왼쪽으로 90도 회전시키는 함수
    def rotate(group):
        for i in range(len(group)):
            r, c = group[i]
            group[i] = [c, -r]  # 왜 이런 값이 되는지는 자료구조상으로 이해하기 (판 전체를 90도 돌린다고 생각)

    n = len(game_board)  # 게임보드 크기 구함
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 시계방향
    answer = 0

    # 블럭, 빈칸 찾음
    block = finding(table, 1)  # 테이블에서 블럭 찾기
    blank = finding(game_board, 0)  # 게임 보드에서 빈칸 찾기

    # 블럭들을 문자열로 해싱해 딕셔너리에 저장
    for i in range(len(block)):
        block[i] = hashing(block[i])

    tmp = dict()  # 딕셔너리
    # 해싱값이 키, 값은 개수가 됨 (같은 모양 블럭 두 개면 값이 2가 되는 방식)
    for hashing_value in block:
        tmp[hashing_value] = tmp.get(hashing_value, 0) + 1
    block = tmp  # 블럭 정보 딕셔너리값으로 갱신

    # 빈칸드 순회하며 해당 빈칸을 4번 90도씩 회전하며 모양 맞는 블럭이 있는지 탐색
    # 있으면 블럭 딕셔너리의 값(개수)-1
    for i in range(len(blank)):
        for _ in range(4):  # 네 번 회전
            rotate(blank[i])  # 빈칸을 회전
            hash_blank = hashing(blank[i])  # 빈칸 해싱해 문자열로 받아옴
            if block.get(hash_blank):  # 모양 맞는 블럭 있으면
                block[hash_blank] -= 1  # 개수 하나 차감

                # 해시값 길이가 실제 빈칸 수 *2이므로(행,열) 2로 나눠 리턴값에 추가
                answer += len(hash_blank) // 2
                break  # 다음 블럭 확인 위함
    return answer
