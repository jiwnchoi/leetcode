class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        sum_grid = [
            [
                0 for _ in range(len(grid[0]) + 1)
            ]
            for _ in range(len(grid) + 1)
        ]
        ans = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                sum_grid[y+1][x+1] = sum_grid[y+1][x] + sum_grid[y][x+1] + grid[y][x] - sum_grid[y][x]

                if sum_grid[y+1][x+1] <= k:
                    ans +=1

        return ans