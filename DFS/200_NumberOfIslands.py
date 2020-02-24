# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0
        if grid is None or len(grid) == 0:
            return 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):

                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count = count + 1

        return count

    def dfs(self, grid, i, j):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = 'X'

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

# In that case, there are N*M vertexes and slightly less than 4*N*M edges, their sum is still O(N*M)
# T (E+V) = O(m*n)  S O(1)

