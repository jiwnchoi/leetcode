class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        def dfs(current: int, path: list[int]):
            if current == len(graph) -1:
                paths.append([*path, current])
            else:
                for n in graph[current]:
                    if n not in path:
                        dfs(n, [*path, current])
        dfs(0, [])
        return paths