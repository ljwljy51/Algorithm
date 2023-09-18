#https://school.programmers.co.kr/learn/courses/30/lessons/1845
#해시

def solution(nums):
    return len(set(nums)) if (len(set(nums))<len(nums)//2) else len(nums)//2
#unique한 폰켓몬 수가 전체 폰켓몬 수//2보다 적으면 unique한 폰켓몬 수 리턴, 아니면 전체 폰켓몬 수 //2 리턴
#"중복"고려해야 할 경우 set사용하면 좋음 