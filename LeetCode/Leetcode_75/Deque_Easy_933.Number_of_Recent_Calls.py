# 클래스 구현 문제는 처음이라 좀 헤맴
from collections import deque


class RecentCounter:
    def __init__(self):
        self.dq = deque()

    def ping(self, t: int) -> int:
        self.dq.append(t)  # request time 추가

        while t - self.dq[0] > 3000:  # 3000ms 이전 내 이뤄진 호출이 아닌 경우
            self.dq.popleft()  # 제거

        return len(self.dq)  # 이전 3000ms 내 request 수 리턴


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
