#https://www.youtube.com/watch?v=0Umai2XnxzA
from collections import defaultdict
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        comb_list = list(zip(timestamp, username, website))
        comb_list.sort()

        visit_hm = defaultdict(list)
        for t, u, w in comb_list:
            visit_hm[u].append(w)
        
        scores = defaultdict(int)
        for user, websites in visit_hm.items():
            for pattern in set(combinations(websites, 3)):
                scores[pattern] += 1
        
        max_pattern, max_score = [], 0
        for pattern, score in scores.items():
            if score > max_score or (score == max_score and pattern < max_pattern):
                max_pattern = pattern 
                max_score = score
        return max_pattern

