# https://leetcode.com/problems/merge-intervals/description/

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        if intervals is None:
            return None

        n = len(intervals)
        start = []
        end = []

        for i in range(0, n):
            start.append(intervals[i][0])
            end.append(intervals[i][1])

        start.sort()
        end.sort()

        startOfMergedInterval = 0
        currentInterval = 0
        res = []

        for currentInterval in range(0, n):

            if currentInterval == n - 1 or start[currentInterval + 1] > end[currentInterval]:
                res.append([start[startOfMergedInterval], end[currentInterval]])
                startOfMergedInterval = currentInterval + 1

        return res
# T O(nlogn) S O(n)
