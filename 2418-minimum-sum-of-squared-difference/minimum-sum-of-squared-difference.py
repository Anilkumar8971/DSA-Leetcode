# Binary Approach method
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        k = k1 + k2
        diffs = [abs(a-b) for a, b in zip(nums1, nums2)]
        if sum(diffs) <= k:
            return 0
        low, high = 0, max(diffs)
        target_ceiling = high
        while low <= high:
            mid = (low + high) // 2
            ops = sum(max(0,d-mid) for d in diffs)
            if ops <= k:
                target_ceiling = mid
                high = mid -1
            else:
                low = mid + 1
        for i in range(len(diffs)):
            if diffs[i] > target_ceiling:
                k -= diffs[i] - target_ceiling
                diffs[i] = target_ceiling
        for i in range(len(diffs)):
            if k == 0:
                break
            if diffs[i] == target_ceiling and diffs[i] > 0:
                diffs[i] -= 1
                k -= 1
        return sum(d * d for d in diffs)