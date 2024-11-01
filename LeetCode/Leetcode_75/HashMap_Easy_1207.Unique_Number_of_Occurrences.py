from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt_dict = defaultdict(int)
        for elem in arr:
            cnt_dict[elem] += 1

        return len(cnt_dict) == len(set(cnt_dict.values()))
