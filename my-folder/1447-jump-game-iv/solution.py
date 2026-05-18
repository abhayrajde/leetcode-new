from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        valToInd = defaultdict(list)

        for i, val in enumerate(arr):
            valToInd[val].append(i)

        q = deque([0])
        visited = {0}
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                neighbors = []

                neighbors.append(i - 1)
                neighbors.append(i + 1)

                neighbors.extend(valToInd[arr[i]])

                for nei in neighbors:
                    if 0 <= nei < n and nei not in visited:
                        visited.add(nei)
                        q.append(nei)

                # VERY IMPORTANT OPTIMIZATION
                valToInd[arr[i]].clear()

            steps += 1
