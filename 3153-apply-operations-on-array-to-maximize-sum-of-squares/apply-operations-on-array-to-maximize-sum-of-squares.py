class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        bit_counts = [0] * 31
        for num in nums:
            for b in range(31):
                if (num >> b) & 1:
                    bit_counts[b]+=1
        ans = 0
        for _ in range(k):
            val = 0
            for b in range(31):
                 if bit_counts[b] > 0:
                     val |= 1 << b
                     bit_counts[b] -= 1
            ans = (ans + val * val) % MOD
        return ans

        