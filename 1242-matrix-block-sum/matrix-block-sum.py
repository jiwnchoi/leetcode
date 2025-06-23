class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        max_y = len(mat)
        max_x = len(mat[0])

        answer = [[
            0 for _ in range(max_x)
        ] for _ in range(max_y) ]

        for y in range(max_y):
            for x in range(max_x):
                start_x = max(x-k, 0)
                end_x = min(x+k+1, max_x)

                start_y = max(y-k, 0)
                end_y = min(y+k+1, max_y)

                submat = mat[start_y:end_y]
                submat = [ row[start_x:end_x] for row in submat ]
                answer[y][x] = sum(sum(submat, []))

        return answer

