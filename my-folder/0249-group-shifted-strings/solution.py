from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_signature(s):
            if len(s) == 1:
                return ('single',)
            return tuple((ord(s[i + 1]) - ord(s[i])) % 26 for i in range(len(s) - 1))
    
        groups = defaultdict(list)
        
        for s in strings:
            signature = get_signature(s)
            groups[signature].append(s)
    
        return list(groups.values())
