class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        is_sorted = True
        for i in range(1, n):
            if s[i] < s[i - 1]:
                is_sorted = False
                break
        if is_sorted:
            return 0
        if n <= 2:
            return -1
        min_char = min(s)
        max_char = max(s)
        if s[0] == min_char or s[-1] == max_char:
            return 1
        if min_char in s[:-1] or max_char in s[1:]:
            return 2
        return 3