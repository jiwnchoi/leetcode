class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def get_neighbors(pos: tuple[int, int]) -> list[tuple[int, int]]:
            y, x = pos
            return [
                pos for pos in [
                    (y+1, x) if y+1 <= len(board) -1 else None,
                    (y, x+1) if x+1 <= len(board[0]) -1 else None,
                    (y-1, x) if y-1 >= 0 else None,
                    (y, x-1) if x-1 >= 0 else None,
                ] if pos
            ]
        
        def get_char(pos: tuple[int, int]) -> str:
            return board[pos[0]][pos[1]]

        def is_word(visited: list[tuple[int, int]]) -> bool:
            n = len(visited) -1
            pos = visited[n]
            if get_char(pos) == word[n] and n == len(word) -1:
                return True
            
            if get_char(pos) == word[n]:
                neighbors = get_neighbors(pos)
                for neighbor in neighbors:
                    if neighbor in visited:
                        continue

                    if is_word([*visited, neighbor]):
                        return True
                        

            return False


        for y in range(len(board)):
            for x in range(len(board[0])):
                if is_word([(y, x)]):
                    return True

        return False
