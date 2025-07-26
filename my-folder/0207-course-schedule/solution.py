class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        visited = set()

        def dfs(crs):
            # Base Case
            if prereq[crs] == []:
                return True

            if crs in visited:
                return False

            visited.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            prereq[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        



