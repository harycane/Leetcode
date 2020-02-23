# https://leetcode.com/problems/top-k-frequent-words/description/


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        bucket = [None] * (len(words) + 1)
        freq_map = {}

        for word in words:
            if word in freq_map:
                freq_map[word] = freq_map[word] + 1
            else:
                freq_map[word] = 1

        for key, val in freq_map.items():

            if bucket[val] is None:
                bucket[val] = [key]
            else:
                bucket[val].append(key)

        n = len(bucket)
        res = []

        for i in range(n - 1, -1, -1):
            if bucket[i] is not None:
                temp_ls = bucket[i]
                temp_ls.sort()
                for temp in temp_ls:
                    res.append(temp)
                    if len(res) == k:
                        return res

        return res

    # T O(n + nlogn) = T O(nlogn) S O(n)
