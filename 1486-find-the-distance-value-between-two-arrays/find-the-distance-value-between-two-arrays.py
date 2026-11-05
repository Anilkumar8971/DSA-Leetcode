class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        cnt = 0
        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                cnt += 1
        return cnt