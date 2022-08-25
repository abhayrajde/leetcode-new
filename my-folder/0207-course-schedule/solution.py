class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        prereq = {c:[] for c in range(numCourses)}
        
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        visited = set()
        cycle = set()
        def dfs(crs):
            if(crs in cycle):
                return False
            if(crs in visited):
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if(dfs(pre)==False):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            return True
        
        for crs in range(numCourses):
            if(dfs(crs) == False):
                return False
        return True
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
