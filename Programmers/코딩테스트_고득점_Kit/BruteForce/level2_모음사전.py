# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 어떻게 접근해야할지 감을 못잡아 헤맸다.
# 중복순열을 만들어주는 product 사용
# 그동안 permutations, combinations만 써왔는데, product 있는 걸 처음 알았음
# product 함수 사용법에 유의
# 이것도 역시나 입력의 크기가 크지 않아서 가능했던 풀이인듯

from itertools import product


def solution(word):
    alpha_lst = ["A", "E", "I", "O", "U"]
    words_lst = []
    for i in range(1, 6):  # 길이 1~5
        for w in product(alpha_lst, repeat=i):  # 중복순열 만들어 하나씩 받아옴
            words_lst.append("".join(list(w)))  # 리스트로 변환해 join해주는 것에 유의

    words_lst.sort()  # 정렬
    return words_lst.index(word) + 1  # 특정 요소의 인덱스 알려주는 함수
