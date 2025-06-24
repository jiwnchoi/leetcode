class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        diff_x = abs(fx - sx)
        diff_y = abs(fy - sy)

        min_t = min(diff_x, diff_y) + diff_x + diff_y - min(diff_x, diff_y) * 2
        max_t = diff_x + diff_y
        
        if diff_x == diff_y == 0 and t == 1:
            return False
        print(diff_x, diff_y, t)
        return min_t <= t 