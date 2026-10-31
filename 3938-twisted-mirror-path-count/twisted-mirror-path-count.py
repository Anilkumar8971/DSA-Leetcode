class Solution(object):
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        memo_r = {}
        memo_d = {}
        def get_dest(r, c, direction):
            if r < 0 or r >= m or c < 0  or c >= n:
                return None
            if grid[r][c] == 0:
                return (r, c)
            if direction == 0:
                if (r, c) not in memo_r:
                    memo_r[(r, c)] = get_dest(r + 1, c, 1)
                return memo_r[(r, c)]
            else:
                if (r, c) not in memo_d:
                    memo_d[(r, c)] = get_dest(r, c + 1, 0)
                return memo_d[(r, c)]
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for r in range(m):
            for c in range(n):
                val = dp[r][c]
                if val == 0 or grid[r][c] == 1:
                    continue
                dest_r = get_dest(r, c + 1, 0)
                if dest_r is not None:
                    nr, nc = dest_r
                    dp[nr][nc] = (dp[nr][nc] + val) % MOD
                dest_d = get_dest(r + 1, c, 1)
                if dest_d is not None:
                    nr, nc = dest_d
                    dp[nr][nc] = (dp[nr][nc] + val) % MOD
        return dp[m - 1][n - 1]