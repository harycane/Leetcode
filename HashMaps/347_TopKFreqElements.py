# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        bucket = [None] * (len(nums) + 1)
        freq_map = {}

        for val in nums:
            if val in freq_map:
                freq_map[val] = freq_map[val] + 1
            else:
                freq_map[val] = 1

        for key, val in freq_map.items():

            if bucket[val] is None:
                bucket[val] = [key]
            else:
                bucket[val].append(key)

        res = []

        n = len(bucket)

        for i in range(n - 1, -1, -1):

            if bucket[i] is not None:
                temp_ls = bucket[i]
                for temp in temp_ls:
                    if len(res) == k:
                        return res
                    res.append(temp)

        return res

        # T O(n) S O(n)