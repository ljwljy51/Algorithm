import sys
import heapq

input = sys.stdin.readline

n = int(input())
answer = 0  # 매수해야 하는 사람 수
if n == 1:  # 혼자 출마했을 경우
    input()  # 입력 처리
    print(0)
    exit(0)
else:
    current = int(input())  # 다솜의 현재 득표 수 입력받음
    vote_lst = []  # 나머지 사람들의 득표 수
    for i in range(n - 1):
        heapq.heappush(vote_lst, -1 * int(input()))  # 최대 득표수가 맨 앞에 오게 하기 위해 -1을 곱해줌

while True:
    max_vote = -1 * heapq.heappop(vote_lst)  # 최대 득표 수
    if current > max_vote:  # 다솜이 표 제일 많이 받게 됐으면
        break
    else:
        max_vote -= 1  # 표 감소
        current += 1  # 다솜 표 증가
        answer += 1  # 매수한 사람 수
        heapq.heappush(vote_lst, -1 * max_vote)  # 다시 힙에 넣어줌

print(answer)
