class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum < 1 or sum > 9 * num:
            return ""
        count_9 = sum // 9
        remainder = sum % 9
        count_rem = 1 if remainder > 0 else 0
        count_0 = num - count_9 - count_rem
        parts = ["9" * count_9]
        if remainder > 0:
            parts.append(str(remainder))
        parts.append("0" * count_0)
        return "".join(parts)