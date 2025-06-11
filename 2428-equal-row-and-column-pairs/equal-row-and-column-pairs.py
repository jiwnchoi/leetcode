from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_hm = {}
        result = 0

        for i, row in enumerate(grid):
            if tuple(row) in row_hm:
                row_hm[tuple(row)] += 1
            else:
                row_hm[tuple(row)] = 1

        for i in range(len(grid[0])):
            col_key = tuple([row[i] for row in grid])
            if col_key in row_hm:
                result += row_hm[col_key]

        return result