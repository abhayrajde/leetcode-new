class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(list)
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        cycle = set()
        def dfs(crs):
            if prereq[crs] == []:
                return True

            if crs in cycle:
                return False

            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            prereq[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
                

