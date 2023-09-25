# 이미 예전에 풀었던 문제인데, 조건이 추가되어 코드를 수정해줬다.
# https://rain-bow.tistory.com/30
# 위 풀이를 참고했다.


def solution(n, lost, reserve):
    lost_mod = list(set(lost) - set(reserve))
    reserve_mod = list(set(reserve) - set(lost))  # 여분 가져왔는데 도난당한 경우 고려 위함
    reserve_mod.sort()

    for reserve_num in reserve_mod:  # 왼쪽부터 검사. 비교 기준을 "빌려주는 사람"으로 해야 함. 이걸 캐치 못해서 헤맴
        if reserve_num - 1 in lost_mod:
            lost_mod.remove(reserve_num - 1)
        elif reserve_num + 1 in lost_mod:
            lost_mod.remove(reserve_num + 1)
    return n - len(lost_mod)
