# class Solution(object):
#     def minMoves(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         min_val = min(nums)
#         return sum(x - min_val for x in nums)

class Solution(object):

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)