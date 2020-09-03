# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if target >= letters[-1]:  # > or 'equal' to is important
            return letters[0]  # wraps around to return first letter if all elements in list is less than target

        lo = 0
        hi = len(letters) - 1

        while lo < hi:

            mid = (lo + hi) // 2

            if letters[mid] <= target:

                lo = mid + 1
            else:
                hi = mid

        return letters[lo]

    # T O(logN)

#         for letter in letters:
#             if letter > target:
#                 # return first occurence
#                 return letter

#         return letters[0] # since they wrap around, if not returned yet, return the first char
# T O(n) can do better since list is sorted





