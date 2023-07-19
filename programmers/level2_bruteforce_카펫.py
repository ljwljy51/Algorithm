#https://school.programmers.co.kr/learn/courses/30/lessons/42842

def getCarpetHeight(n):  # t세로가 가로보다 더 짧다는 점을 고려
    height_lst = []
    for i in range(3, int(n**(1/2)) + 1):  # 노란 격자 있어야 하므로 최소 세로 길이 3임
        if (n % i == 0):  # 약수 중 작은 수만 append
            height_lst.append(i)

    return height_lst


def solution(brown, yellow):
    total = brown+yellow  # 총 격자 개수
    possible_height_lst = getCarpetHeight(total)  # 카펫의 세로 길이 계산

    for height in possible_height_lst:
        width = total//height  # 카펫 가로 길이 계산
        if width*2+(height-2)*2 == brown:  # 갈색 격자와 수 같으면 결과 계산해 리턴
            return [width, height]
