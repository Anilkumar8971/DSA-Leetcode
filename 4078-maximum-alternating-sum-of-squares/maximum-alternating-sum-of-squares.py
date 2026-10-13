class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(x * x for x in nums)
        k = len(nums) // 2
        return sum(a[k:]) - sum(a[:k])
        