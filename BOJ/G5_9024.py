import sys

input = sys.stdin.readline

t = int(input())  # 테스트 케이스 수
for _ in range(t):
    n, K = map(int, input().split())
    lst = list(map(int, input().split()))  # 수 입력받음
    lst.sort()  # 이분탐색 위해 정렬
    stat = float("inf")  # 타겟과의 차이 측정 위함
    answer = 0
    for i in range(n):
        # 이분탐색
        target = K - lst[i]  # 타겟 계산
        left = i + 1
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            diff = abs(K - (lst[i] + lst[mid]))
            if diff < stat:  # 차이가 더 적게 나는 경우
                stat = diff  # 상태 갱신
                answer = 1
            elif diff == stat:  # 기존 차이와 같은 경우
                answer += 1

            if lst[mid] < target:  # 찾는 값이 절반 기준 오른쪽에 있으면
                left = mid + 1
            elif lst[mid] > target:  # 찾는 값이 절반 기준 왼쪽에 있으면
                right = mid - 1
            else:  # 타겟 찾은 경우
                break

    print(answer)
