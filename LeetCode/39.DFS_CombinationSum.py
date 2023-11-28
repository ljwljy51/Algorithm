# DFS 사용
# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(current_val, idx, comb_stat):
            if current_val < 0:  # 0보다 작아지면 조건 만족 x
                return
            if current_val == 0:  # 0으로 떨어지면 조건 만족
                answer.append(comb_stat[:])  # 지금까지의 조합 append

            for i in range(idx, len(candidates)):  # 현재 인덱스 기준으로 모든 경우에 대해 dfs 호출
                dfs(current_val - candidates[i], i, comb_stat + [candidates[i]])

        dfs(target, 0, [])
        return answer
