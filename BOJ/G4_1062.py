import sys
from itertools import combinations
input=sys.stdin.readline

n,k=map(int, input().split())
words=[input()[4:-4] for _ in range(n)] #앞, 뒤 부분 제외하고 입력 받음
default={'a', 'n', 't', 'i', 'c'} #이 다섯 개 단어는 반드시 가르쳐야 함

if k<5:#가르칠 수 있는 단어가 5개보다 적은 경우
    print(0) #읽을 수 있는 단어 없음
    sys.exit()

if k==26: #모든 알파벳 가르치는 경우
    print(n) #모든 단어 읽을 수 있음
    sys.exit()
    
not_learned=[]
for i in range(26):
    if chr(i+97) not in default: #안 배운 알파벳들 넣어줌
        not_learned.append(chr(i+97))
        
answer=0
for comb in combinations(not_learned, k-5): #가르칠 수 있는 가능한 모든 조합에 대해 확인
    cnt=0
    for word in words: #입력에서 앞 뒤 잘라낸 단어에 대해
        for char in word: #알파벳 하나씩 분리해서 봄
            if char not in default and char not in comb: #해당 단어를 배우지 못한 경우
                break
        else:
            cnt+=1 #단어 읽을 수 있는 경우
    answer=max(answer, cnt) #더 큰 값을 갖는 것이 최종 정답. 
    #for문 돌며 가르칠 수 있는 모든 가능한 알파벳 조합에 대해 검사
    
print(answer)
        