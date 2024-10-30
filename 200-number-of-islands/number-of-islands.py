class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def is_position_valid(y: int, x: int):
            return 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x] == "1" and visited[y][x] == False

        def get_neighbors(y: int, x:int):
            candidates = [
                (y+1, x),
                (y-1, x),
                (y, x+1),
                (y, x-1)
            ]
            return [
                (y, x) for y, x in candidates if is_position_valid(y, x)
            ]

        def dfs(y: int, x: int):
            stack = [(y, x)]
        
            while len(stack):
                current = stack.pop()
                y, x = current
                visited[y][x] = True   

                neighbors = get_neighbors(y, x)
                print(current, neighbors)
                stack.extend(neighbors)

        n = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "0" or visited[y][x]:
                    continue
                    
                n += 1
                dfs(y,x)

        return n