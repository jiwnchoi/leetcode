from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = defaultdict(list)

        for edge in prerequisites:
            if edge[1] == edge[0]:
                return False
            hm[edge[1]].append(edge[0])

        visited = [0 for _ in range(numCourses)]

        def has_cycle(source):
            if visited[source] == 1:
                return True
            if visited[source] == 2:
                return False
            
            visited[source] = 1

            for target in hm[source]:
                if has_cycle(target):
                    return True
            
            visited[source] = 2
            return False

        for source in list(hm.keys()):
            if visited[source] == 0 and has_cycle(source):
                return False
        
        return True


"""
시간 복잡도: O(numCourses + )
"""