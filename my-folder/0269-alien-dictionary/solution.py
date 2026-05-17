class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = { c: set() for w in words for c in w }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w2[j]].add(w1[j])
                    break
        
        cycle = set() # stores letters that are part of current cycle | helps in detecting cycle
        visited = set() # stores letters that are already visited
        res = []

        def dfs(c):
            # Base Cases
            if c in cycle:
                return True
            if c in visited:
                return False

            cycle.add(c)
            for nei in adj[c]:
                if dfs(nei): return True
            cycle.remove(c)
            visited.add(c)
            res.append(c)

        for c in adj:
            if dfs(c): return ""
        # res.reverse()
        return "".join(res)

