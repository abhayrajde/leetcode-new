class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # Maybe DP
        visited = set()
        def dfs(ind, visited):
            # Base Cases
            if ind < 0 or ind >= len(arr) or ind in visited:
                return False

            if arr[ind] == 0:
                return True
                
            visited.add(ind)
            left = dfs(ind - arr[ind], visited)
            right = dfs(ind + arr[ind], visited)
            visited.remove(ind)

            return left or right
        return dfs(start, visited)

