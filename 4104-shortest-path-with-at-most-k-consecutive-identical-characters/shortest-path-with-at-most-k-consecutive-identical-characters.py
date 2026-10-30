from heapq import heappop, heappush
class Solution(object):
    def shortestPath(self, n, edges, labels, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        best = [k + 1] * n
        heap = [(0, 1, 0)]
        while heap:
            d, run, x = heappop(heap)
            if run >= best[x]:
                continue
            if x == n - 1:
                return d
            best[x] = run
            for y, w in graph[x]:
                r = run + 1 if labels[y] == labels[x] else 1
                if r <= k and r < best[y]:
                    heappush(heap, (d + w, r, y))
        return -1
        