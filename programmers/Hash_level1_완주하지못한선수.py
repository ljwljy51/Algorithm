#https://school.programmers.co.kr/learn/courses/30/lessons/42576
#해시

def solution(participant, completion):
    dict={} #딕셔너리에 이름 별 참가자 수 저장(동명이인 고려)
    for person in participant: 
        if person not in dict: 
            dict[person]=1
        else:
            dict[person]+=1
    
    for com_person in completion:
        dict[com_person]-=1
        if dict[com_person]==0:
            del dict[com_person]
    
    for key,value in dict.items():
        return key #남아있는 참가자 이름 출력