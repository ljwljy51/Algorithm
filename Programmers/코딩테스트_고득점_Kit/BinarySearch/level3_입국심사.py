# https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9E%85%EA%B5%AD%EC%8B%AC%EC%82%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 애초에 방법을 너무 잘못생각하고 있었음
# input의 최대길이가 지나치게 길고, 특정 값을 찾아야 하는 문제라면 이분탐색을 의심
# 이분 탐색을 할 때는 ‘이분 탐색의 범위는 무엇으로 할지’ 와 ‘이분 탐색의 기준을 무엇으로 할지’를 고려해야 함
def solution(n, times):
    # 가능한 최대, 최소 시간을 right, left로 지정
    left = 1
    right = max(times) * n  # 모든 사람들이 가장 오래 걸리는 사람한테서 받을 경우

    while left <= right:  # 이분탐색
        mid = (left + right) // 2  # 기준 설정
        people = 0  # 심사한 사람 수

        for time in times:
            # 각 심사대에서 주어진 시간동안 심사받은 사람 수를 더함
            people += mid // time

            # n명보다 많이 심사 가능한 경우 break
            if people >= n:
                break

        if people >= n:  # n명보다 더 만이 심사했으면 시간이 너무 많이 주어진 것
            # 딱 n명 심사했더라도 시간이 남을 가능성 존재
            answer = mid
            right = mid - 1
        else:  # n명 미만 심사했다면 시간이 너무 부족한 것
            left = mid + 1
    return answer
