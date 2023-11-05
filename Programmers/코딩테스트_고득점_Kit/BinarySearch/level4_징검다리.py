# https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 처음에 풀었으나, 이분탐색 기준을 뭐로 잡아야 할지 몰라 이분탐색을 안썼더니 시간초과 났었다
# 그래서 결국 또 솔루션 봐버렸다..^^ 어쩌지 정말
# n개의 돌을 제거하기 위한 돌 사이 간격의 최적의 값을 찾는 문제
# 이분 탐색을 할 때는 ‘이분 탐색의 범위는 무엇으로 할지’ 와 ‘이분 탐색의 기준을 무엇으로 할지’를 고려해야 함


def solution(distance, rocks, n):
    start = 1
    end = distance  # 시작점, 도착점 지정

    rocks.sort()  # 이분탐색 위해 정렬
    rocks.append(distance)

    while start <= end:
        mid = (start + end) // 2
        del_stone_cnt = 0  # 제거한 돌의 수
        current_stone = 0  # 기준
        for rock in rocks:
            if rock - current_stone < mid:  # 현재 돌 사이의 거리가 가정한 값보다 작으면 제거
                del_stone_cnt += 1
            else:  # 가정한 값보다 거리가 크면 그 돌을 새로운 기준으로 세움
                current_stone = rock

            if del_stone_cnt > n:  # 더 많이 제거했으면
                break

        if del_stone_cnt > n:  # 돌이 많이 제거된 경우
            end = mid - 1  # 기준을 더 낮춤
        else:  # 돌이 덜 혹은 알맞게 제거된 경우
            answer = mid
            start = mid + 1  # 기준을 더 높임

    return answer
