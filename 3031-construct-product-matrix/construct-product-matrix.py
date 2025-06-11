class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        fg = [val for row in grid for val in row]

        prefix_mul = [ 1 for _ in fg ]
        suffix_mul = [ 1 for _ in fg ]

        prefix_mul[0] = fg[0]
        suffix_mul[-1] = fg[-1]

        for i in range(len(fg)):
            if i > 0:
                prefix_mul[i] = (prefix_mul[i-1] % 12345) * (fg[i] % 12345)
                suffix_mul[-i-1] = (suffix_mul[-i] % 12345) * (fg[-i-1] % 12345)
        
        output = [
            [
                0 for val in row
            ]
            for row in grid
        ]
        for i in range(len(fg)):
            x = i % len(grid[0])
            y = i // len(grid[0])

            if i == 0:
                output[y][x] = suffix_mul[1] % 12345
            elif i == len(fg)-1:
                output[y][x] = prefix_mul[len(fg)-2]% 12345
            else:
                output[y][x] = (prefix_mul[i-1] * suffix_mul[i+1]) % 12345

        return output
                