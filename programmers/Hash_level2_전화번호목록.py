#https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    phone_book.sort()  # 정렬
    current_num = phone_book[0]  # 비교 기준
    for i in range(1, len(phone_book)):
        if current_num == phone_book[i][: len(current_num)]:  # 만약 접두사에 해당할 경우
            return False
        else:  # 접두사 아닐 경우
            current_num = phone_book[i]

    return answer
