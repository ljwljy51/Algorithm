# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        mid = (start + end) >> 1

        result = guess(mid)
        while result != 0:
            if result == 1:
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end) >> 1
            result = guess(mid)

        return mid
