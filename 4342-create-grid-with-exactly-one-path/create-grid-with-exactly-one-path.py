class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid = [["#"] * n for _ in range(m)]
        for c in range(n):
            grid[0][c] = "."
        for r in range(m):
            grid[r][n - 1] = "."
        return ["".join(row) for row in grid]