class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        n_col = len(grid[0])
        n_row = len(grid)

        dp = [[dict() for _ in range(n_col)] for _ in range(n_row)]

        dp[0][0][grid[0][0]] = 1

        for row in range(n_row):
            for col in range(n_col):
                if row == col == 0:
                    continue


                if row > 0:
                    for xor, paths in dp[row-1][col].items():
                        xor = xor ^ grid[row][col]
                        dp[row][col][xor] = dp[row][col].get(xor, 0) + paths

                if col > 0:
                    for xor, paths in dp[row][col-1].items():
                        xor = xor ^ grid[row][col]
                        dp[row][col][xor] = dp[row][col].get(xor, 0) + paths

        
        return 0 if k not in dp[n_row-1][n_col-1] else int(dp[n_row-1][n_col-1][k] % (1000000000 + 7))


        