from collections import deque

def solution(begin, target, words):
    d = deque([begin]) #초기값 넣어줌
    cnt = 0 # 몇 바퀴 돌았는지 확인 위함
    while len(d) != 0: #덱이 빌 때까지
        cnt += 1 #한 번 덱 비울 때마다 1씩 증가
        for _ in range(len(d)):
            begin = d.pop() #시작 단어 추출
            for word in words:
                diff_cnt = 0
                for i in range(len(begin)): #글자 다른 개수 확인
                    if begin[i] != word[i]: 
                        diff_cnt += 1

                if diff_cnt == 1: #다른 글자 수가 1개인 경우
                    d.appendleft(word) #그 단어를 덱에 넣어둠
                    words.remove(word) #단어 리스트에서 해당 단어 삭제
            
        if target in d: #덱에 target이 있는지 확인
            return cnt

    return 0