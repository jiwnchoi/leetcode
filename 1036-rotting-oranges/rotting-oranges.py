class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_y = len(grid) -1
        max_x = len(grid[0])-1

        def get_safe_pos(y, x):
            return [
            p for p in [
                (y, x+1) if x < max_x and grid[y][x+1] == 1 else None,
                (y, x-1) if x > 0 and grid[y][x-1] == 1 else None,
                (y+1, x) if y < max_y and grid[y+1][x] == 1 else None,
                (y-1, x) if y > 0 and grid[y-1][x] == 1 else None,
            ] if p is not None]
        
        i = -1
        changed = True

        while changed:
            i +=1 
            changed = False
            
            new_grid = [
                [
                    cell for cell in row
                ] for row in grid
            ]
            
            for y in range(max_y + 1):
                for x in range(max_x + 1):
                    if grid[y][x] == 2:
                        poses = get_safe_pos(y,x)
                        for pos in poses:
                            p_y, p_x = pos
                            new_grid[p_y][p_x] = 2
                            changed = True
            grid = new_grid

        has_fresh = False
        for y in range(max_y+1):
            for x in range(max_x+1):
                if grid[y][x] == 1:
                    has_fresh = True

        if has_fresh:
            return -1
        else:
            return i


        
        


                    
                            