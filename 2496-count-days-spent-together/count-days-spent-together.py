class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        prefix = [0, 31, 59, 90,120,151,181,212,243,273,304,334]
        def to_day(date):
            month, day = int(date[:2]), int(date[3:])
            return prefix[month - 1] + day
        start = max(to_day(arriveAlice), to_day(arriveBob))
        end = min(to_day(leaveAlice), to_day(leaveBob))
        return max(0, end - start + 1)