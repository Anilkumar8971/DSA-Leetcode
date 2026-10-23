class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        displaced = [num for i, num in enumerate(nums) if num != i]
        if not displaced:
            return 0
        ans = displaced[0]
        for num in displaced[1:]:
            ans &= num
        return ans  