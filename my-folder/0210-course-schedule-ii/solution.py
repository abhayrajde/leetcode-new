class Solution:
    def findOrder(self, numCourses, prerequisites):
        preMap = {c:[] for c in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        visited, cycle = set(), set()
        result = []

        def dfs(crs):
            #Base Cases
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            result.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return result

        
