from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0
        row_hm = Counter(tuple(row) for row in grid)

        for i in range(len(grid[0])):
            col_key = tuple([row[i] for row in grid])
            if col_key in row_hm:
                result += row_hm[col_key]

        return result

# 시간 복잡도: O(len(grid)^2) 
# 해시 과정에서의 시간 복잡도 주의