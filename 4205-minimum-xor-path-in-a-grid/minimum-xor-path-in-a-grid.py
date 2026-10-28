class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        for c in range(1, n):
            val = grid[0][c]
            dp[c] = {x ^ val for x in dp[c - 1]}
        for r in range(1, m):
            new_dp = [set() for _ in range(n)]
            val = grid[r][0]
            new_dp[0] = {x ^ val for x in dp[0]}
            for c in range(1, n):
                val = grid[r][c]
                combined = dp[c] | new_dp[c -1]
                new_dp[c] = {x ^ val for x in combined}
            dp = new_dp
        return min(dp[n - 1])