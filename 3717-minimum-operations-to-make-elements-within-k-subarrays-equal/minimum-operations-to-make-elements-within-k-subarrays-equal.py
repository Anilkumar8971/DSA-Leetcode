class Window:
    """A sorted window that keeps the sum of its h = x // 2 smallest values."""
    def __init__(self, values: List[int]):
        self.h = len(values) // 2
        self.odd = len(values) & 1
        self.sorted = SortedList(values)
        self.low = sum(self.sorted[: self.h])
        self.total = sum(values)
    @property
    def cost(self) -> int:
        return self.total - 2 * self.low - self.odd * self.sorted[self.h]
    def slide(self, out: int, new: int) -> int:
        s, h = self.sorted, self.h
        if new < s[h - 1]:
            self.low += new - s[h - 1]
        s.add(new)
        if out <= s[h - 1]:
            self.low += s[h] - out
        s.remove(out)
        self.total += new - out
        return self.cost
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        win = Window(nums[:x])
        cost = [win.cost] + [win.slide(out, new)for out, new in zip(nums, nums[x:])]
        best = [0] * (len(nums) + 1)
        for _ in range(k):
            best = list(            accumulate(
                [inf] * x + [b + c for b, c in zip(best, cost)], min
                )
             )
        return best[-1]
        