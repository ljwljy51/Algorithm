import sys
import heapq

input = sys.stdin.readline

n = int(input())
rooms = []

for i in range(n):
    start, end = map(int, input().split())
    rooms.append((start, end))

rooms.sort()  # 시작 시간 기준으로 정렬

end_time = []
heapq.heappush(end_time, rooms[0][1])  # 첫 번쨰 강의의 끝나는 시간 넣어둠

for i in range(1, n):
    if rooms[i][0] < end_time[0]:  # 현재 강의 끝나는 시간보다 다음 강의 시작 시간이 빠르면
        heapq.heappush(end_time, rooms[i][1])  # 새로운 강의실 필요
    else:  # 현재 강의에 이어서 할 수 있으면
        heapq.heappop(end_time)  # 기준 다시 잡기 위함
        heapq.heappush(end_time, rooms[i][1])  # 강의 끝나는 시간 넣어줌


print(len(end_time))
