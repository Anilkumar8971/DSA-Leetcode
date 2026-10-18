class Solution(object):

    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        # Step 1: Precompute Pascal's triangle
        C = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        # Step 2: Define helper outside the Pascal loop
        def count_ways(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            interleave = C[len(left) + len(right)][len(left)]
            return (interleave * count_ways(left) * count_ways(right)) % MOD

        # Step 3: Return the answer excluding the original array
        return (count_ways(nums) - 1 + MOD) % MOD