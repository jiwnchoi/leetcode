class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        max_y = len(heights) -1 
        max_x = len(heights[0])-1

        def get_dir(y, x):
            pos = []
            if y > 0:
                pos.append((y-1, x))
            if x > 0:
                pos.append((y, x-1))
            if y < max_y:
                pos.append((y+1, x))
            if x < max_x:
                pos.append((y, x+1))
            return [ p for p in pos if heights[p[0]][p[1]] >= heights[y][x] ]
        
        pacific = set()
        atlantic = set()

        for x in range(max_x + 1):
            stack = [(0, x)]
            while stack:
                current = stack.pop()
                pacific.add(current)
                next_dirs = get_dir(current[0], current[1])
                stack.extend([d for d in next_dirs if d not in pacific])

        for y in range(max_y + 1):
            stack = [(y, 0)]
            while stack:
                current = stack.pop()
                pacific.add(current)
                next_dirs = get_dir(current[0], current[1])
                stack.extend([d for d in next_dirs if d not in pacific])

        for x in range(max_x + 1):
            stack = [(max_y, x)]
            while stack:
                current = stack.pop()
                atlantic.add(current)
                next_dirs = get_dir(current[0], current[1])
                stack.extend([d for d in next_dirs if d not in atlantic])
        for y in range(max_y + 1):
            stack = [(y, max_x)]
            while stack:
                current = stack.pop()
                atlantic.add(current)
                next_dirs = get_dir(current[0], current[1])
                stack.extend([d for d in next_dirs if d not in atlantic])
        return list(pacific & atlantic)





        