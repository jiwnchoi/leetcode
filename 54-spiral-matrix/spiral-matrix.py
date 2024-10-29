class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.position = (0,0)
        self.directions = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]

        self.directionIndex = 0
        self.visited = set()

        def getCurrentDirection():
            return self.directions[self.directionIndex]

        def getNextDirectionIndex():
            return (self.directionIndex + 1) % 4

        def getMovedPosition():
            return (self.position[0]+getCurrentDirection()[0], self.position[1] + getCurrentDirection()[1])

        def isPositionValid(p: tuple[int, int]):
            return 0<= p[0] < len(matrix) and 0<= p[1] < len(matrix[0])

        def isDiscovered(p: tuple[int, int]):
            return p in self.visited

        def getValue(p: tuple[int, int]):
            return matrix[p[0]][p[1]]

        def getNextPosition():
            nextPosition = getMovedPosition()

            if not isPositionValid(nextPosition) or isDiscovered(nextPosition):
                self.directionIndex = getNextDirectionIndex()
                return getMovedPosition()
            
            return nextPosition
            
            

        values = []

        for _ in range(len(matrix) * len(matrix[0])):
            
            value = getValue(self.position)
            values.append(value)
            self.visited.add(self.position)
            self.position = getNextPosition()


        return values
            