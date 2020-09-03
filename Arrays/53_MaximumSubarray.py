# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # https://github.com/nirmalnishant645/LeetCode/blob/master/0053-Maximum-Subarray.py

        if len(nums) == 0:
            return 0

        maxSum = nums[0]
        runningSum = nums[0]

        for i in range(1, len(nums)):

            if runningSum < 0:
                runningSum = nums[i]
            else:
                runningSum = nums[i] + runningSum

            if runningSum > maxSum:
                maxSum = runningSum

        return maxSum

    # T O(n) S O(1)
    # Kadane algo