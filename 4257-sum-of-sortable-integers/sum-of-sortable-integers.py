class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Precompute the sorted version to quickly check block boundaries
        sorted_nums = sorted(nums)
        def is_valid_k(k):
            # Check each block of size k
            for start in range(0, n, k):
                block = nums[start : start + k]
                # 1. Check if the block's min and max match the sorted array's boundaries
                # In the fully sorted array, this block spans [start, start + k - 1]
                if min(block) != sorted_nums[start] or max(
                    block
                ) != sorted_nums[start + k - 1]:
                    return False
                # 2. Check if the block can be sorted via cyclic rotation
                # Count cyclic drops: block[j] > block[(j + 1) % k]
                drops = 0
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        drops += 1
                        if drops > 1:
                            return False
            return True
        # Find all divisors of n
        divisors = []
        for d in range(1, int(n**0.5) + 1):
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
        ans = 0
        for k in divisors:
            if is_valid_k(k):
                ans += k
        return ans