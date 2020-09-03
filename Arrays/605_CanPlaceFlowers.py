# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        cnt = 0
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] != 1) and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] != 1):
                flowerbed[i] = 1
                cnt += 1

            if cnt >= n:
                return True

        return False

    # T O(n)