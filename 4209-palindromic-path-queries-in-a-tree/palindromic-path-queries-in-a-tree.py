import sys
sys.setrecursionlimit(200000)
class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 2)
    def update(self, idx, val):
        while idx <= self.size:
            self.tree[idx] ^= val
            idx += idx & -idx
    def query(self, idx):
        res = 0
        while idx > 0:
            res ^= self.tree[idx]
            idx -= idx & -idx
        return res

class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOGN = 17
        up = [[0] * LOGN for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        stack = [(0, -1, 0)]
        depth[0] = 0
        while stack:
            u, p, state = stack.pop()
            if state == 0:
                timer += 1
                tin[u] = timer
                up[u][0] = p if p != -1 else 0
                for i in range(1, LOGN):
                    up[u][i] = up[up[u][i - 1]][i - 1]
                stack.append((u, p, 1))
                for v in adj[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOGN):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOGN - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]
        bit = FenwickTree(n)
        char_list = list(s)
        for u in range(n):
            char_mask = 1 << (ord(char_list[u]) - ord("a"))
            bit.update(tin[u], char_mask)
            bit.update(tout[u] + 1, char_mask)
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_c = parts[2]
                old_c = char_list[u]
                if old_c != new_c:
                    delta = (1 << (ord(old_c) - ord("a")))^(1 << (ord(new_c) - ord("a")))
                    bit.update(tin[u], delta)
                    bit.update(tout[u] + 1, delta)
                    char_list[u] = new_c
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                mask_u = bit.query(tin[u])
                mask_v = bit.query(tin[v])
                lca_char_mask = 1 << (ord(char_list[lca]) - ord("a"))
                path_mask = mask_u ^ mask_v ^ lca_char_mask
                can_form = (path_mask & (path_mask - 1)) == 0
                ans.append(can_form)
        return ans