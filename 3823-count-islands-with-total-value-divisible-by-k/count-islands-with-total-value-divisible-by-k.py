from collections import deque
class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        valid_islands = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    island_sum = grid[r][c]
                    grid[r][c] = 0
                    queue = deque([(r, c)])
                    while queue:
                        cr, cc = queue.popleft()
                        for dr, dc in ((-1, 0), (1,0), (0,-1), (0, 1)):
                            nr = cr + dr
                            nc = cc + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = (
                                    0
                                )
                                queue.append((nr, nc))
                    if island_sum % k == 0:
                        valid_islands += 1
        return valid_islands           
