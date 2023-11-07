# https://www.ai-bio.info/programmers/1843
# DP 너무너무 어렵다.. 솔루션 보고도 이해하는 데 좀 시간이 걸렸다.
# 부호, 숫자의 위치는 절대 변하면 안됨
# 최댓값을 구하기 위해서는 덧셈 뒤에 나오는 수는 가장 커져야 하고, 뺄셈 뒤에 나오는 수는 가장 작아져야 함
# 가장 큰 값의 경우를 저장하는 DP뿐만 아니라, 가장 작은 값의 경우를 저장하는 DP 또한 추가적으로 생성 필요
# MAX_DP[i][j] = nums[i] 부터 nums[j] 까지 연산했을 때 최댓값
# MIN_DP[i][j] = nums[i] 부터 nums[j] 까지 연산했을 때 최솟값
# 단, DP는 이차원 배열, 각 차원의 길이는 숫자의 개수만큼
# i < k <= j 인 k를 생각하여 i~j 구간이 i~k-1, k~j 의 두 구간으로 나뉨
# op[k-1]의 종류에 따라서 max_dp[(i, j)]와 min_dp[(i, j)]계산을 위해 기억해둘 값이 달라진다


def solution(arr):
    max_dp = {}
    min_dp = {}
    nums = [int(x) for x in arr[::2]]
    ops = [x for x in arr[1::2]]

    for i in range(len(nums)):  # 자기 자신에 대한 연산 결과
        max_dp[(i, i)] = nums[i]
        min_dp[(i, i)] = nums[i]

    for interval in range(1, len(nums)):  # 각 구간 별 계산 위함
        for i in range(len(nums)):  # 구간 시작점
            j = i + interval  # 구간 끝점 계산
            if j >= len(nums):  # 인덱스 오류 방지 위함
                continue

            max_candidates, min_candidates = [], []  # 최대, 최소값 후보 저장 위함

            for k in range(
                i + 1, j + 1
            ):  # i < k <= j 인 k를 생각하여 i~j 구간이 i~k-1, k~j 의 두 구간으로 나뉨
                if ops[k - 1] == "-":  # 뺄셈 연산을 해야 하는 경우
                    max_candidates.append(
                        max_dp[(i, k - 1)] - min_dp[(k, j)]
                    )  # 해당 구간 내에서 최대값-최소값의 계산 결과가 저장되도록 함
                    min_candidates.append(
                        min_dp[(i, k - 1)] - max_dp[(k, j)]
                    )  # 해당 구간 내에서 최소값-최대값의 계산 결과가 저장되도록 함
                else:
                    max_candidates.append(
                        max_dp[(i, k - 1)] + max_dp[(k, j)]
                    )  # 해당 구간 내에서 최대값+최대값의 계산 결과가 저장되도록 함
                    min_candidates.append(
                        min_dp[(i, k - 1)] + min_dp[(k, j)]
                    )  # 해당 구간 내에서 최소값+최소값의 계산 결과가 저장되도록 함
            max_dp[(i, j)] = max(max_candidates)  # i~j구간 사이에서의 최대값 저장
            min_dp[(i, j)] = min(min_candidates)  # i~j구간 사이에서의 최소값 저장

    return max_dp[(0, len(nums) - 1)]  # 전체 구간에서의 최대값 리턴
