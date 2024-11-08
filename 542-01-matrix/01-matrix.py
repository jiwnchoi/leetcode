class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        counts = [[1e5 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        for y in range(len(mat)):
            for x in range(len(mat[0])):
                if mat[y][x] == 0:
                    counts[y][x] = 0
                    continue
                counts[y][x] = min(
                    counts[y-1][x] + 1 if y > 0 else 1e5,
                    counts[y][x-1] + 1 if x > 0 else 1e5
                )
                

        

        for y in range(len(mat)-1, -1, -1):
            for x in range(len(mat[0])-1, -1, -1):
                counts[y][x] = min(
                    counts[y+1][x] + 1 if y < len(mat) -1 else 1e5,
                    counts[y][x+1] + 1 if x < len(mat[0]) -1 else 1e5,
                    counts[y][x]
                )

        return counts

                



