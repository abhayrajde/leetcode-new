class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        prereq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        # print(prereq)
        visited = set()

        def dfs(crs):
            # Base Case Scenarios:
            if crs in visited:
                return False
            if prereq[crs] == []:
                return True

            visited.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            prereq[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
