class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less_count = 0
        target_count = 0
        # count the elements smaller than and equal to target
        for num in nums:
            if num < target:
                less_count += 1
            elif num == target:
                target_count += 1
        # The indices will start at `less_count` and span `target_count` places
        return [less_count + i for i in range(target_count)]

        # or
        
class Solution(object):
    def targetIndices(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        return[i for i,val in enumerate(nums) if val == target]
