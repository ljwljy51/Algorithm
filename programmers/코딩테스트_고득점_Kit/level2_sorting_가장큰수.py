def solution(numbers):
    # 원소 별 최대값이 1000임을 고려해 각 정수를 string으로 변환해 *3해준 뒤 정렬
    # ex) "30", "3"이 주어졌을 때 , "303030"과 "333"이 비교되어 "333"이 우선순위로 정렬됨
    #''.join()을 통해 리스트 안의 각 요소를 concat해줌
    # numbers 리스트 안의 요소가 모두 0일 때를 고려해 정렬된 결과의 첫 원소가 0일 경우 "0" 리턴

    answer = "".join(
        sorted(list(map(str, numbers)), key=lambda x: (x * 3), reverse=True)
    )
    return "0" if answer[0] == "0" else answer
