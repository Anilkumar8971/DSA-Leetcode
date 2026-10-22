class Solution(object):

    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0

        # Check if nums is an increasing cyclic shift or decreasing cyclic shift
        is_inc = True
        is_dec = True

        for i in range(n):
            next_val = nums[(i + 1) % n]
            if (next_val - nums[i]) % n != 1:
                is_inc = False
            if (nums[i] - next_val) % n != 1:
                is_dec = False

        if not is_inc and not is_dec:
            return -1

        p = nums.index(0)

        ans = float("inf")

        if is_inc:
            # 1. Pure left rotations
            ans = min(ans, p)
            # 2. Reverse -> left rotate -> reverse: effectively rotating right (n - p) times
            if p > 0:
                ans = min(ans, (n - p) + 2)

        if is_dec:
            # 1. Reverse first, then left rotate:
            # After reverse, 0 is at index n - 1 - p. Then (n - 1 - p) left rotations.
            ans = min(ans, 1 + (n - 1 - p))
            # 2. Left rotate first, then reverse:
            # Rotate left until 0 is at index n - 1, which takes (p + 1) % n steps, then 1 reverse.
            ans = min(ans, 1 + ((p + 1) % n))

        return ans