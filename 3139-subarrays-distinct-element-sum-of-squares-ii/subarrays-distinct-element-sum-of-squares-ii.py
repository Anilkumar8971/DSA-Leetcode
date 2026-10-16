class BIT(object):

    def __init__(self, n):
        self.size = n
        # Preallocated arrays avoid the hash-table lookup overhead of defaultdict
        self.tree1 = [0] * (n + 2)
        self.tree2 = [0] * (n + 2)

    def _lowbit(self, x):
        return x & -x

    def _add(self, idx, delta):
        idx += 1
        raw_idx = idx
        while idx <= self.size:
            self.tree1[idx] += delta
            self.tree2[idx] += (raw_idx - 1) * delta
            idx += self._lowbit(idx)

    def add_range(self, left, right, delta):
        self._add(left, delta)
        self._add(right + 1, -delta)

    def _query(self, idx):
        idx += 1
        if idx > self.size:
            idx = self.size

        raw_idx = idx
        res = 0
        while idx > 0:
            res += raw_idx * self.tree1[idx] - self.tree2[idx]
            idx -= self._lowbit(idx)
        return res

    def query_range(self, left, right):
        if left > right:
            return 0
        return self._query(right) - self._query(left - 1)


class Solution(object):

    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)

        bit = BIT(n + 2)
        seen = {}
        cur = 0
        ans = 0

        for i, val in enumerate(nums):
            # Previous position of `val`, defaults to -1
            prev = seen.get(val, -1)
            j = prev + 1

            # (x + 1)^2 - x^2 = 2x + 1
            # Over the interval [j, i], delta = 2 * sum(x) + length
            cur = (cur + 2 * bit.query_range(j, i) + (i - j + 1)) % MOD
            ans = (ans + cur) % MOD

            # Add 1 to range [j, i]
            bit.add_range(j, i, 1)
            seen[val] = i

        return ans
        