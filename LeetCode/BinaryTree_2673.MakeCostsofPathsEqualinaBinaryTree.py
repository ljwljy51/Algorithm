# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/description/
# iterative
# bottom_up
# graph
# tree


# depth 별로 올라가면서 depth 별 cost 같게 만들어야 함
# 이때, 자식의 cost 정보도 반영해야 함
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        answer = 0  # 총합 담을 변수
        node = n // 2  # depth-1단계에서의 최대 leaf node 번호
        for i in reversed(range(node)):  # 마지막 leaf부터 접근
            left_cost, right_cost = cost[2 * i + 1], cost[2 * i + 2]
            inc_cnt = abs(left_cost - right_cost)  # 각 leaf 쌍 별로 같은 cost 갖도록 증가시켜야 할 횟수
            answer += inc_cnt  # 증가

            is_left_large = left_cost > right_cost  # 어느 쪽 cost가 더 큰지 저장
            cost[i] += (
                left_cost if is_left_large else right_cost
            )  # parent의 cost를 child의 cost만큼 증가시킴

        return answer
