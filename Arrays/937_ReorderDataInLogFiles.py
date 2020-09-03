# https://leetcode.com/problems/reorder-data-in-log-files/description/
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # separate lists for letters and digits in each log
        letters = []
        digits = []

        for log in logs:
            # if the word following the first word is a digit then its a digits log
            if log.split(' ')[1].isdigit():
                digits.append(log)
            # else its a letters log and hence store it in apposite list
            else:
                letters.append(log)

        # python's sorted uses Timsort, a hybrid version of merge and insertion sort with time complexity of nlogn and
        # space complexity of n; key allows custom comparison; a tuple with 1st argument to sort lexicographically,
        # and second args to sort by identifier in case of a tie.
        letters_sorted = sorted(letters, key=lambda letter: (letter.split(' ')[1:], letter.split(' ')[0]))

        # returns the concatenated list containing sorted letters log and digits
        # log with original order of digits in input log
        return letters_sorted + digits

    # T O(m * n log n) - where m is the max len of a single log; n is the no of logs in input list
    # sorting n element logs is n log n; and using each log as key for custom comparison could in worst case incur m
    # S O (m * n) - max len of a log times total no of logs of space
