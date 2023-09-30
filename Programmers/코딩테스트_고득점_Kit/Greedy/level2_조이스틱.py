# https://school.programmers.co.kr/learn/courses/30/lessons/42860
# 또 솔루션 봐버렸다..~
# https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy
# 좌우 이동 최소 조건을 어떻게 구현해야할지 파악을 못했었다.
# 작동 매커니즘 잘 파악하기


def solution(name):
    spell_move = 0  # 상하 이동
    cursor_move = len(name) - 1  # 좌우 이동.

    for i, spell in enumerate(name):
        # 상하 이동 정도 중 최소값 반영
        spell_move += min(ord(spell) - ord("A"), ord("Z") - ord(spell) + 1)

        # 현재 알파벳 기준 다음부터 연속된 A 문자열 찾기
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == "A":  # 다음 글자가 A인 경우
            next_idx += 1
        # 이전 커서 이동 값, 연속된 A의 왼쪽, 연속된 A의 오른쪽 부분 시작 방식 비교해 최소 이동값으로 갱신
        cursor_move = min(
            [
                cursor_move,
                2 * i + (len(name) - next_idx),
                i + 2 * (len(name) - next_idx),
            ]
        )  # 초기 시작 위치가 첫 번째 인덱스기에, 왼쪽/오른쪽 시작 방식에 따라 두 번 왔다갔다하는 곳이 존재함에 유의

    return spell_move + cursor_move
