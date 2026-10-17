class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        n = len(nums)
        target = sorted(nums,key=lambda x: (digit_sum(x), x))
        target_pos = {val: i for i, val in enumerate(target)}
        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or target_pos[nums[i]] == i:
                visited[i] = True
                continue
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = target_pos[nums[curr]]
                cycle_size += 1
            if cycle_size > 1:
                swaps += cycle_size - 1
        return swaps