from collections import deque

def solution(numbers, target):
    d=deque([numbers[0], -numbers[0]]) #초기값 넣어둠
    for i in range(1, len(numbers)):
        for _ in range(len(d)): #덱(큐)이 빌 때까지
            tmp=d.pop()
            d.appendleft(tmp+numbers[i]) #+, -한 결과 모두를 append함
            d.appendleft(tmp-numbers[i])
            
    answer=0
    for result in d: #덱 내부 요소 모두 돌면서 target과 같은 것 있는지 확인
        if result==target:
            answer+=1
        
    return answer